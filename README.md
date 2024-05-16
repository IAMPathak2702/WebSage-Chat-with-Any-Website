Chat-with-Any-Website

## Description
This project is aimed at developing a chatbot for the WordPress site "VectorDatabase" using the Pinecone LLM model from OpenAI. The chatbot facilitates natural language interactions with users visiting the site, providing them with information, answering queries, and assisting them in navigation.

## Features
- Chatbot powered by the Pinecone LLM model
- Integration with WordPress site "VectorDatabase"
- User-friendly UI made with HTML and CSS, utilizing Bootstrap
- RESTful API integration with FastAPI
- Real-time communication using WebSocket

## Technologies Used
- OpenAI Pinecone LLM model
- FastAPI
- HTML/CSS (Bootstrap)
- WebSocket
- WordPress REST API

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/IAMPathak2702/ved-prakash-pathak-wasserstoff-aitask.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Access the application at `http://localhost:8000` in your browser.

## Configuration
Make sure to set the following environment variables:
- `OPENAPI_KEY`: Your OpenAI API Key
- `WORDPRESS_USERNAME`: WordPress username for accessing the site
- `WORDPRESS_PASSWORD`: WordPress password for accessing the site
- `APIURL`: URL for the WordPress REST API

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to add.

## License
This project is licensed under the [MIT License](LICENSE).

## Credits
- [OpenAI](https://openai.com) for providing the Pinecone LLM model
- [FastAPI](https://fastapi.tiangolo.com) for the RESTful API framework
- [Bootstrap](https://getbootstrap.com) for the UI styling
- [WordPress](https://wordpress.org) for the content management system

---

Project Snapshots
# chatbot response
<img src=https://raw.githubusercontent.com/IAMPathak2702/ved-prakash-pathak-wasserstoff-AiTask/main/snapshots/chatbotgif.gif>

## wordpress website
<img src=https://raw.githubusercontent.com/IAMPathak2702/ved-prakash-pathak-wasserstoff-AiTask/main/snapshots/photo_2024-05-06_18-48-47.jpg>

## wordpres plugin setting that fetch data

<img src=https://raw.githubusercontent.com/IAMPathak2702/ved-prakash-pathak-wasserstoff-AiTask/main/snapshots/Screenshot%202024-05-06%20183716.png>

# wordpress plugin

<img src=https://raw.githubusercontent.com/IAMPathak2702/ved-prakash-pathak-wasserstoff-AiTask/main/snapshots/Screenshot%202024-05-06%20183747.png>
