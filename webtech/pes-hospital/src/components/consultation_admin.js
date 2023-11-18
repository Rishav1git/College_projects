import React, { useState, useEffect } from 'react';
import ComponentAdmin from './Component_admin';
import styles from './ConsultationAdmin.module.css';

export default function Consultation_admin() {
  const [appointmentRequests, setAppointmentRequests] = useState([]);

  useEffect(() => {
    const fetchAppointmentRequests = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/appointment-request');
        if (response.ok) {
          const data = await response.json();
          setAppointmentRequests(data);
        } else {
          console.error('Failed to fetch appointment requests');
        }
      } catch (error) {
        console.error('Error fetching appointment requests:', error);
      }
    };

    fetchAppointmentRequests();
  }, []);

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://localhost:3001/api/appointment-request/${id}`, {
        method: 'DELETE',
      });

      console.log('Delete URL:', `http://localhost:3001/api/appointment-request/${id}`);
      console.log('Delete Response:', response);

      if (response.ok) {
        // Refresh the list after successful deletion
        const fetchAppointmentRequests = async () => {
          try {
            const response = await fetch('http://localhost:3001/api/appointment-request');
            if (response.ok) {
              const data = await response.json();
              setAppointmentRequests(data);
            } else {
              console.error('Failed to fetch appointment requests');
            }
          } catch (error) {
            console.error('Error fetching appointment requests:', error);
          }
        };

        fetchAppointmentRequests();
      } else {
        console.error('Failed to delete appointment');
      }
    } catch (error) {
      console.error('Error deleting appointment:', error);
    }
  };

  return (
    <>
      <ComponentAdmin />
      <div className='container'>
        <h1 className={styles.title}>Consultation Details</h1>
        <ul className={styles.list}>
          {appointmentRequests.map((request) => (
            <li key={request._id} className={styles.listItem}>
              <span className={styles.label}>Name:</span> {request.name} <br />
              <span className={styles.label}>Email:</span> {request.email} <br />
              <span className={styles.label}>Phone:</span> {request.phone} <br />
              <span className={styles.label}>Date:</span> {request.date} <br />
              <span className={styles.label}>Time:</span> {request.time} <br />
              <span className={styles.label}>Doctor Name:</span> {request.doctorName} <br />
              <span className={styles.label}>Specialities:</span> {request.doctorSpecialties} <br />
              <button onClick={() => handleDelete(request._id)}>Appointment Done</button>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}
