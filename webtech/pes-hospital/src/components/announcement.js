import React from "react";
import Components from './Component_main';
import styles from './Announcement.module.css';

export default function Announcement() {
  return (
    <div >
      <Components />
      <h1 className={styles.announcementTitle}>No Announcement</h1>
    </div>
  );
}
