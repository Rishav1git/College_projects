// Ambulance_admin.js

import React, { useState, useEffect } from 'react';
import ComponentAdmin from './Component_admin';
import styles from './AmbulanceAdmin.module.css';

export default function Ambulance_admin() {
  const [ambulanceRequests, setAmbulanceRequests] = useState([]);

  useEffect(() => {
    const fetchAmbulanceRequests = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/ambulance-requests');
        if (response.ok) {
          const data = await response.json();
          setAmbulanceRequests(data);
        } else {
          console.error('Failed to fetch ambulance requests');
        }
      } catch (error) {
        console.error('Error fetching ambulance requests:', error);
      }
    };

    fetchAmbulanceRequests();
  }, []);

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://localhost:3001/api/ambulance-request/${id}`, {
        method: 'DELETE',
      });

      console.log('Delete URL:', `http://localhost:3001/api/ambulance-request/${id}`);
      console.log('Delete Response:', response);

      if (response.ok) {
        // Refresh the list after successful deletion
        const fetchAmbulanceRequests = async () => {
          try {
            const response = await fetch('http://localhost:3001/api/ambulance-requests');
            if (response.ok) {
              const data = await response.json();
              setAmbulanceRequests(data);
            } else {
              console.error('Failed to fetch ambulance requests');
            }
          } catch (error) {
            console.error('Error fetching ambulance requests:', error);
          }
        };

        fetchAmbulanceRequests();
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
      <div className={styles.AmbulanceAdminContainer}>
        <h1 className={styles.AmbulanceAdminTitle}>Ambulance Request Detail</h1>
        <ul className={styles.AmbulanceAdminList}>
          {ambulanceRequests.map((request) => (
            <li key={request._id} className={styles.AmbulanceAdminListItem}>
              <span className={styles.AmbulanceAdminLocation}>
                Location: {request.location && request.location.coordinates.join(', ')}
              </span>
              <br />
              <span className={styles.AmbulanceAdminMobileNumber}>
                Mobile Number: {request.mobileNumber}
              </span>
              <button onClick={() => handleDelete(request._id)}>Ambulance sent</button>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}
