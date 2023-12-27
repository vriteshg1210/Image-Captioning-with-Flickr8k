# Image-Captioning-with-Flickr8k

## Project Goal
I created an image captioning model which takes in an image as input and generates a sentence describing what is happening in the image. I have used the Flickr 8k data to train the model. The model has been trained using the Inception V3 model and a combination of RNNs.

## Dataset
Flicket 8k- https://machinelearningmastery.com/develop-a-deep-learning-caption-generation-model-in-python/

## Data Preprocessing
Every image in the Flickr 8k dataset has 5 captions. The model will be trained on this data. We append 'startseq' and 'endseq' at the beginning and ending of each caption so that the model knows the start and end points. We then create the corpus of all the words present in the captions and form a vocabulary for the model. As machines understand numbers and not words, we convert each word into a 300 dimension vector using the pretrained Glove model which can be found here- https://nlp.stanford.edu/projects/glove/ This becomes our first input.

Once the captions are ready, we pass the images through the Inception V3 model and remove the last softmax layer so that we can get a 2048 dimensional feature vector for each image. This becomes our second input.

We should also keep in mind that the caption for an image will be generated one word at a time. Hence we will also be training our model in such fashion. For eg. if we have the caption: "startseq a bunch of people swimming in water endseq.", then will form the sequence as below.

Image_vector + ['startseq']
Image_vector + ['startseq', 'a']
Image_vector + ['startseq', 'a', 'bunch']
Image_vector + ['startseq', 'a', 'bunch', 'of']
Image_vector + ['startseq', 'a', 'bunch', 'of', 'people']
Image_vector + ['startseq', 'a', 'bunch', 'of', 'people','swimming']
and so on...

Please note that instead of words, the 300-dimensional vectors will be input into the model as discussed above.

## Model Architecture
![Project Architecture](architecture.jpeg)

## Evaluation 
The model is evaluated using the BLEU score.

## References

1. https://towardsdatascience.com/intuitive-understanding-of-attention-mechanism-in-deep-learning-6c9482aecf4f?%24Ga=true
2. http://karpathy.github.io/2015/05/21/rnn-effectiveness/
3. https://fairyonice.github.io/Develop_an_image_captioning_deep_learning_model_using_Flickr_8K_data.html
4. http://cs231n.github.io/transfer-learning/
5. https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.pdf
