import React, { useState } from 'react';
import AppointmentCss from './appointment.module.css';

const AppointmentForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    date: '',
    time: '',
    doctorName: '',
    doctorSpecialties: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:3001/api/appointment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      console.log(data);
      alert("Appointment Fixed");

      // Handle success or display an error message to the user
    } catch (error) {
      console.error('Error scheduling appointment:', error);
      // Handle error and display an error message to the user
    }
  };

  return (
    <div className={AppointmentCss.AppointmentForm}>
      <h1>Appointment Form</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Your Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <label htmlFor="phone">Phone:</label>
        <input
          type="tel"
          id="phone"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          required
        />

        <label htmlFor="date">Date:</label>
        <input
          type="date"
          id="date"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />

        <label htmlFor="time">Time:</label>
        <input
          type="time"
          id="time"
          name="time"
          value={formData.time}
          onChange={handleChange}
          required
        />

        <label htmlFor="doctorName">Doctor's Name:</label>
        <input
          type="text"
          id="doctorName"
          name="doctorName"
          value={formData.doctorName}
          onChange={handleChange}
          required
        />

        <label htmlFor="doctorSpecialties">Doctor's Specialties:</label>
        <input
          type="text"
          id="doctorSpecialties"
          name="doctorSpecialties"
          value={formData.doctorSpecialties}
          onChange={handleChange}
          required
        />

        <button type="submit">Schedule Appointment</button>
      </form>
    </div>
  );
};

export default AppointmentForm;
