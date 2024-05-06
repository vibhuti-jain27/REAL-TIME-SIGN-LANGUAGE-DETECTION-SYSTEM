import React from 'react';
import '../../static/css/HeroSection.css';
import axios from 'axios'; // Import Axios for making HTTP requests

const HeroSection = () => {
    const handleClick = async (gestureDataPath) => {
        try {
            // Make a POST request to your Django/Flask backend endpoint
            const response = await axios.post('/detection/recognize_gesture_button/', {
                gesture: gestureDataPath
            });

            // Handle the response from the backend
            console.log('Response:', response.data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const onButtonClick = async () => {
        // Your gesture data path
        const gestureDataPath = 'E:/Placement/Research Paper/Sign Language Detection System/my_flask_app/backend/gestures/0'; // Replace with the actual path to the gesture folder

        // Call the onButtonClick function with the gesture data path
        handleClick(gestureDataPath);
    };
    return (
      <div className="HeroSection">
        <div id="box1"></div>
        <div id="box2">
            <div id="text">
               LETS GET STARTED
            </div>
            <div id="text">
               FOR RECOGNITION
            </div>
            
            <button id="recognizegesture" onClick={onButtonClick}> Recognize Gesture </button>

        </div>
        <div id="box3">
            <div id="container">
                <div id="logo">
                    <img src=""/>
                </div>
                <div id="menu">
                    <ul>
                        <li onClick={() => handleClick('E:/Placement/Research Paper/Sign Language Detection System/my_flask_app/backend/gestures/0')}>Get Started</li>
                        <li>Our Team</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    )
  }

  export default HeroSection
