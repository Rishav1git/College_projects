import React from "react";
import Componentcss from './component_admin_main.module.css';
import image1 from './Hospital.png';
import image2 from './24x7.png';
import image3 from './Announcement.png';
import image4 from './50_years_pes.png';
import image11 from './Pes.png';
import { Link } from 'react-router-dom';

export default function Admin() {
  return (
    <>
       <div className={Componentcss.desktop}>
                <div className={Componentcss.div}>
                    <div className={Componentcss.overlapgroup}>
                        <img className={Componentcss.upfrontresilient} src={image1} />
                        <div className={Componentcss.rectangle}>
                        </div>
                        <Link to='/' className={Componentcss.textwrapper}>Admin Logout</Link>
                        
                    </div>
                    <Link to='/Admin'><img className={Componentcss.element} src={image11} /></Link>
                    <Link to='/announcement'><img className={Componentcss.istockphoto} src={image3} /></Link>
                    <img className={Componentcss.pes} src={image4} />
                    <div className={Componentcss.textwrapper5}>ADMIN</div>
                    <img className={Componentcss.elementemergency} src={image2} />
                </div>
            </div>    
    </>
  );
}
