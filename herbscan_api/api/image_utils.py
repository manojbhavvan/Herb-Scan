import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load the trained model
model = tf.keras.models.load_model(
    "D:/Projects/Herb-Scan/Herb-Scan/herbscan_api/api/plant_identification_model.h5"
)

label_mapping = {
    0: "Abutilon Indicum (Thuthi)",
    1: "Alpinia Galanga (Rasna)",
    2: "Amaranthus Viridis (Arive-Dantu)",
    3: "Artocarpus Heterophyllus (Jackfruit)",
    4: "Azadirachta Indica (Neem)",
    5: "Basella Alba (Basale)",
    6: "Brassica Juncea (Indian Mustard)",
    7: "Carissa Carandas (Karanda)",
    8: "Citrus Limon (Lemon)",
    9: "Ficus Auriculata (Roxburgh fig)",
    10: "Ficus Religiosa (Peepal Tree)",
    11: "Hibiscus Rosa-sinensis",
    12: "Jasminum (Jasmine)",
    13: "Mangifera Indica (Mango)",
    14: "Mentha (Mint)",
    15: "Moringa Oleifera (Drumstick)",
    16: "Muntingia Calabura (Jamaica Cherry-Gasagase)",
    17: "Murraya Koenigii (Curry)",
    18: "Nerium Oleander (Oleander)",
    19: "Nyctanthes Arbor-tristis (Parijata)",
    20: "Ocimum Tenuiflorum (Tulsi)",
    21: "Piper Betle (Betel)",
    22: "Plectranthus Amboinicus (Mexican Mint)",
    23: "Pongamia Pinnata (Indian Beech)",
    24: "Psidium Guajava (Guava)",
    25: "Punica Granatum (Pomegranate)",
    26: "Santalum Album (Sandalwood)",
    27: "Syzygium Cumini (Jamun)",
    28: "Syzygium Jambos (Rose Apple)",
    29: "Tabernaemontana Divaricata (Crape Jasmine)",
    30: "Trigonella Foenum-graecum (Fenugreek)",
}


# Load and preprocess the image
def preprocess_image(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    preprocessed_image = preprocess_input(image_array)
    return preprocessed_image


# Perform prediction
def predict_plant(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)

    # Map model's numeric predictions to labels
    predicted_label_index = np.argmax(predictions)
    predicted_label = label_mapping[predicted_label_index]
    confidence = predictions[0][predicted_label_index]

    return predicted_label, confidence
