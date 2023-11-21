import React, { useState, useEffect } from 'react';
import Components from './Component_main';
import Doctordetailcss from './Doctor_detail.module.css';

const Doctor_detail = () => {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    const fetchDoctors = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/doctors');
        if (!response.ok) {
          throw new Error(`Error fetching doctors: ${response.statusText}`);
        }
        const data = await response.json();
        console.log('Doctors Data:', data); // Log the received data
        setDoctors(data);
      } catch (error) {
        console.error('Error fetching doctors:', error.message);
      }
    };

    fetchDoctors();
  }, []);

  return (
    <>
      <Components />
      <div className={Doctordetailcss.doctordetails}>
        <h2>Doctors</h2>
        <ul>
          {doctors.map((doctor) => (
            <li key={doctor._id}>
              <h3>Name: {doctor.name}</h3>
              <p>Qualification: {doctor.qualification}</p>
              <p>Specialization: {doctor.specialization}</p>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
};

export default Doctor_detail;
