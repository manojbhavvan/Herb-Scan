# HerbScan API

The HerbScan API is a powerful tool for classifying Ayurvedic plant species using a MobileNet ML model. This API allows users to upload images of plants and receive predictions about their species along with confidence scores.
This API is already deployed in render. [herb-scan.onrender.com](https://herb-scan.onrender.com/)

## API Endpoints

### `/upload` (POST)

**Description:** Uploads an image of an Ayurvedic plant for classification.

**Request:**
- Method: POST
- Headers: Content-Type: multipart/form-data
- Body: Image file

**Response:**
```json
{
    "predicted_label": "Mentha (Mint)",
    "confidence": 0.9990418553352356
}
```

**Sample Usage (Python - Requests):**
```python
import requests

url = 'https://herb-scan.onrender.com/upload/'
files = {'image': open('path/to/your/image.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())
```
**Getting Started**
To use the HerbScan API, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.
3. Start the Django server by running python manage.py runserver.
4. Use the provided API endpoints to upload images and receive predictions.

**Sample Response**
After uploading an image, you will receive a response similar to the following:
```json
{
    "predicted_label": "Mentha (Mint)",
    "confidence": 0.9990418553352356
}
```

Contributing
Contributions to the HerbScan API are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
You can copy and paste this code into your `README.md` file on GitHub and adjust any details as needed.
