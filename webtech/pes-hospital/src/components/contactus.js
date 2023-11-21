import React from "react";
import Components from './Component_main';
import styles from './Contact.module.css';

export default function Contact() {
  return (
    <div >
      <Components />
      <h1 className={styles.contactTitle}>Contact Us</h1>
      <p className={styles.contactText}>
        {`
          Thank you for considering PES University Hospital. If you have any inquiries, need assistance, or would like to schedule an appointment, please feel free to reach out to us using the following contact information:

          Hospital Address:
          PES University Hospital
          VM67+HVP, Hosur Rd, Konappana Agrahara, Electronic City, Bengaluru, Karnataka 560100

          Phone:
          Main Reception: 9380005636
          Emergency Services: 7483172096
          General Inquiries: 8722658530

          Email:
          General Inquiries: info@pesuhospital.com
          Appointments: appointments@pesuhospital.com
          Emergency: emergency@pesuhospital.com

          Working Hours:
          Monday to Friday: 8:00 AM - 8:00 PM
          Saturday: 9:00 AM - 4:00 PM
          Sunday:Holiday
          Emergency Services (24x7)

          Appointment Booking:
          To schedule an appointment, you can call our appointments line during working hours or use our online appointment booking system on our website.

          Emergency Services:
          For medical emergencies, please call our emergency services number immediately. In case of life-threatening situations, dial your local emergency number.

          Connect with Us:
          Stay connected with PES University Hospital through our social media channels for updates, health tips, and community events.
        `}
      </p>
      
    </div>
  );
}

