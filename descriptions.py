# opening text file
PATH = 'C:/Users/vrite/Documents/Image Captioning with Flickr8k/ImageCaptioning/Flickr8k_text'
with open(PATH+"/Flickr8k.token.txt") as f:
    data = f.read()
	
# dictionary contining key as image_id and value as list of captions.
descriptions = dict()

try:
    for el in data.split("\n"):
        tokens = el.split()
        # Check if the line has the expected number of tokens
        if len(tokens) < 2:
            continue  # Skip lines with insufficient tokens
        image_id , image_desc = tokens[0],tokens[1:]

        # dropping .jpg from image id
        image_id = image_id.split(".")[0]

        image_desc = " ".join(image_desc)
        
        # check if image_id is already present or not
        if image_id in descriptions:
            
            descriptions[image_id].append(image_desc)
        else:
            descriptions[image_id] = list()
            descriptions[image_id].append(image_desc)
except Exception as e: 
    print("Exception got :- \n",e)

print(descriptions["1000268201_693b08cb0e"])