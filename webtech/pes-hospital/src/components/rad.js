// rad.js

import React from "react";
import Components from './Component_main';
import styles from './Rad.module.css';

export default function Rad() {
  return (
    <div className={styles.radContainer}>
      <Components />
      <h1 className={styles.radTitle}>R&D</h1>
      <p className={styles.radText}>
        At PES University Hospital, our unwavering commitment to excellence extends beyond patient care to the forefront of Research and Development (R&D). Our dedicated R&D endeavors are integral to our mission of redefining medical standards and advancing healthcare innovation. Through a collaborative and multidisciplinary approach, our skilled team of researchers explores new horizons in medical science, technology, and patient care methodologies. The R&D initiatives at PES University Hospital are designed to pioneer breakthroughs in diagnostics, treatment modalities, and healthcare delivery, ensuring that we continuously elevate the standards of medical practice. By fostering a culture of inquiry, experimentation, and knowledge-sharing, we empower our researchers to contribute meaningfully to the evolution of medical knowledge. Through these efforts, PES University Hospital remains at the forefront of medical advancements, positioning itself as a leader in not just healthcare provision but also in shaping the future of medicine.
      </p>
    </div>
  );
}
