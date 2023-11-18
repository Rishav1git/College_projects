import React from 'react';
import {
 BrowserRouter as Router,
 Routes,
 Route
} from "react-router-dom";
import Main from './components/Component_main';
import Doctor from './components/Doctor_detail';
import Menu from './components/menu';
import Ambulance from './components/Ambulance.js';
import Login from './components/admin_login.js';
import Patient from './components/patient';
import Labtest from './components/labtest.';
import Pharmacy from './components/pharmacy';
import Consultation from './components/consultation';
import About from './components/about';
import Rad from './components/rad';
import Departments from './components/deprtments';
import Contact from './components/contactus';
import Register from './components/Appointment.js';
import Announcement from './components/announcement';
import Admin from './components/Admin.js';
import Ambulance_admin from './components/Ambulance_admin.js';
import Consultation_admin from './components/consultation_admin.js';

function App() {
 return (
   <Router>
     <Routes>
     <Route path="/Admin" element={<><Admin/></>} />
     <Route path="/Ambulance_admin" element={<><Ambulance_admin/></>} />
     <Route path="/consultation_admin" element={<><Consultation_admin/></>} />
       <Route path="/" element={<><Main/><Menu/></>} />
       <Route path="/Doctor_detail" element={<Doctor/>} />
       <Route path="/patient" element={<Patient/>} />
       <Route path="/pharmacy" element={<Pharmacy/>} />
       <Route path="/labtest" element={<Labtest/>} />
       <Route path="/consultation" element={<Consultation/>} />
       <Route path="/Ambulance" element={<Ambulance/>} />
       <Route path="/about" element={<About/>} />
       <Route path="/contactus" element={<Contact/>} />
       <Route path="/rad" element={<Rad/>} />
       <Route path="/departments" element={<Departments/>} />
       <Route path="/admin_login" element={<><Login/></>} />
       <Route path="/announcement" element={<Announcement/>} />
       <Route path="/registration" element={<><Main/><Register/></>} />
     </Routes>
   </Router>
 );
}

export default App;
