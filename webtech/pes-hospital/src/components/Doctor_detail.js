import React from "react";
import Components  from './Component_main';
import Doctordetailcss from './Doctor_detail.module.css'

const Doctor_detail = (props) => {
    const { name, specialization, contact } = props;
  
    return (
        <>
      <Components/>
      <div className={Doctordetailcss.doctordetails}>
        <h3>Name: {name}</h3>
        <p>Specialization: {specialization}</p>
        <p>Contact: {contact}</p>
      </div>
      </>
    );
  };
  
  export default Doctor_detail;