import React, { useState } from 'react';
import Components from './Component_main';
import Ambulancecss from './Ambulance.module.css';
import image1 from './Ambulance.png';
import image2 from './call.png';

export default function Ambulance() {
  const [mobileNumber, setMobileNumber] = useState('');

  const getLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          console.log('Latitude:', latitude);
          console.log('Longitude:', longitude);
          console.log('Mobile Number:', mobileNumber);

          sendAmbulanceRequest({ latitude, longitude, mobileNumber });
        },
        (error) => {
          console.error('Error getting location:', error.message);
        }
      );
    } else {
      console.error('Geolocation is not supported by this browser.');
    }
  };

  const sendAmbulanceRequest = async (requestData) => {
    try {
      const response = await fetch('http://localhost:3001/api/ambulance/request', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      const data = await response.json();
      console.log(data);

      // Handle success or display an error message to the user
      alert('Request Sent For Ambulance');
    } catch (error) {
      console.error('Error sending ambulance request:', error);
      // Handle error and display an error message to the user
    }
  };

  return (
    <>
      <Components />
      <div className={Ambulancecss.desktop}>
        <div className={Ambulancecss.div}>
          <img className={Ambulancecss.element} src={image1} />
          <div className={Ambulancecss.formWrapper}>
            <div className={Ambulancecss.formGroup}>
              <label htmlFor="mobileNumber">Mobile Number:</label>
              <input
                type="tel"
                id="mobileNumber"
                name="mobileNumber"
                value={mobileNumber}
                onChange={(e) => setMobileNumber(e.target.value)}
                placeholder="Enter your mobile number"
              />
            </div>
            <div className={Ambulancecss.overlapgroup} onClick={getLocation}>
              <div className={Ambulancecss.textwrapper}>CALL AMBULANCE</div>
              <img className={Ambulancecss.untitled} src={image2} alt="call icon" />
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
