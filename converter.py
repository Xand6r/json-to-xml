import sys
import json

# a function to convert a json object into xml
def json2xml(json_obj, line_padding=""):
    # create a list to hold the content of our XML
    result_list = list()
    # check if the object passed is a list or an object
    json_obj_type = type(json_obj)
    
    # if we are dealing with a list
    if json_obj_type is list:
        # go through each element
        for sub_elem in json_obj:
            # for each of the elements in the array, call the function on them, the function would return an XML which we would then add to the result_list array
            result_list.append(json2xml(sub_elem, line_padding))
        # return the content of the array, which are XML lines seperated by new linese.g "<ALEX> 123 </ALEX> \n <NEW> 456 </NEW>""
        return "\n".join(result_list)
    
    # if we are dealing with an object
    if json_obj_type is dict:
        # go through the keys of the dicitonary
        for tag_name in json_obj:
            # get the value of the key in the object
            sub_obj = json_obj[tag_name]
            # begin the XML with the key e.g <ALEX>
            result_list.append("%s<%s>" % (line_padding, tag_name))
            # between the opening and closing tags of the XML call the function recursively on the content of the object, for any nested objects
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            # end the XML with the key e.g </ALEX>
            result_list.append("%s</%s>" % (line_padding, tag_name))
        #      
        return "\n".join(result_list)
    
    # if we pass neither an object nor an array, we just return back whatever we passed into the function
    return "%s%s" % (line_padding, json_obj)

# the main body of the script
if __name__ == "__main__":
    # if the number of arguments are incorrect,alert the user
    if len(sys.argv) != 2:
        print("incorrect number of arguments, the function recieves an argument which is the name of the json file")
    else:
        # read in the argument which should be the filename
        filename=sys.argv[1]
        # open the file
        try:
            with open (filename) as json_file:
                # read in the json from it
                # try parsing the file as json
                try:
                    json_data = json.load(json_file)
                
                # if there was an errorr, then alert us the error was from not being able to parse the file as json
                except json.decoder.JSONDecodeError:
                    print("there was an error parsing this file as json, try another")
                    sys.exit()
                # if the file is is good condition, convert it to xml
                output_xml = json2xml(json_data)

                # create a new file with a filename as the input file.xml.xml and write the json to it
                new_filename=filename.split(".")[0] + "xml.xml"
                with open(new_filename,"w") as write_file:
                    write_file.write(output_xml)
                    
        except FileNotFoundError:
        #     # if there is an error , meaninng the fine doesnt exist
            print("file doesn't exist, please cross check the name:",filename)




    
