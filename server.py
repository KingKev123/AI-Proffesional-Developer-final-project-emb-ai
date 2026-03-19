"""
Flask application for emotion detection.
This module provides a web interface for detecting emotions in text using Watson NLP.
"""

from flask import Flask, render_template, request
from flask_cors import CORS
from EmotionDetection import emotion_detector

app = Flask(__name__)
CORS(app, origins="*")

@app.after_request
def add_security_headers(response):
    """Add security headers to all responses."""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    
    Returns:
        str: Rendered HTML template for the index page
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_app():
    """
    Handle emotion detection requests.
    
    Gets text from query parameters, analyzes emotions, and returns formatted response.
    For invalid input, returns error message.
    
    Returns:
        if (!request.body || typeof request.body !== "object") {
          return reply.code(400).send({ error: "Invalid request body" });
        }
        str: Formatted emotion analysis result or error message
    """
    # Get the text from the request arguments
    if (!request.body || typeof request.body !== "object") {
      return reply.code(400).send({ error: "Invalid request body" });
    }
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (error case)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Create the formatted response string for valid input
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

    return formatted_response


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    is_production = any([
        os.environ.get('FLASK_ENV') == 'production',
        os.environ.get('ENV') == 'production',
        os.environ.get('ENVIRONMENT') == 'production',
        os.environ.get('PYTHON_ENV') == 'production'
    ])
    if is_production:
        debug_mode = False
    else:
        debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
