// About.js

import React from "react";
import Components from './Component_main';
import styles from './About.module.css';

export default function About() {
  return (
    <div >
      <Components />
      <h1 className={styles.aboutTitle}>About Us</h1>
      <p className={styles.aboutText}>
        Welcome to PES University Hospital, where our commitment to excellence in healthcare is unwavering. Established with a vision to redefine medical care, we pride ourselves on a legacy of compassion, innovation, and expertise. At PES University Hospital, we bring together a dedicated team of skilled healthcare professionals who are driven by a shared mission to provide comprehensive and patient-centric medical services. Our state-of-the-art facilities are equipped with cutting-edge technology, ensuring the highest standards of diagnosis, treatment, and care. As a leading healthcare institution, we prioritize the well-being of our patients, striving to create a healing environment that fosters trust and comfort. Our multidisciplinary approach, coupled with a focus on research and education, positions PES University Hospital at the forefront of medical advancements. Thank you for choosing us as your healthcare partner, and we look forward to accompanying you on your journey to optimal health and wellness.
      </p>
    </div>
  );
}
