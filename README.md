# InspireTheSouls - Crystal Recommender

A web application that provides personalized crystal recommendations based on birth energy and intentions.

## Features

- Personalized crystal recommendations based on:
  - Birth date (Zodiac sign)
  - Numerology (Root and Destiny numbers)
  - Personal intentions
- Detailed crystal information including:
  - Healing properties
  - Elemental associations
  - Chakra connections
  - Usage instructions
- Responsive design for all devices
- Secure and production-ready

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Rohit7594/InspireTheSouls
cd crystal_recommender
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Deployment

The application is ready for deployment on platforms like Heroku, PythonAnywhere, or any WSGI-compatible hosting service.

### Environment Variables

- `FLASK_ENV`: Set to 'development' for development mode
- `PORT`: Port number for the application (default: 5000)

### Production Considerations

- The application uses Gunicorn as the WSGI server
- Security headers are configured for production use
- Error pages are implemented for common HTTP errors
- Content Security Policy is configured for secure resource loading

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Project Structure

```
crystal_recommender/
├── app.py              # Main Flask application
├── templates/
│   └── index.html     # HTML template
├── static/
│   └── styles.css     # CSS styles
├── data/
│   ├── zodiac_crystals.json
│   └── numerology_crystals.json
├── utils/
│   └── helpers.py     # Helper functions
├── requirements.txt
└── README.md
```

## Future Enhancements

- Add user intentions/goals for more personalized recommendations
- Implement user accounts and save recommendations
- Add crystal descriptions and images
- Create an API for integration with other platforms
- Enhance mobile responsiveness 
