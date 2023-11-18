import React from 'react';
import Componentcss from './component_main.module.css';
import {Link} from 'react-router-dom';
import image1 from './Hospital.png';
import image2 from './24x7.png';
import image3 from './Announcement.png';
import image4 from './50_years_pes.png';
// import image10 from './Ambulance.png';
import image11 from './Pes.png';

export default function Main() {
 return(
            <div className={Componentcss.desktop}>
                <div className={Componentcss.div}>
                    <div className={Componentcss.overlapgroup}>
                        <img className={Componentcss.upfrontresilient} src={image1} />
                        <div className={Componentcss.rectangle}>
                        </div>
                        <Link to='/' className={Componentcss.textwrapper}>Home</Link>
                        <Link to='/about' className={Componentcss.textwrapper2}>About Us</Link>
                        <Link to='/rad' className={Componentcss.rd}>R&amp;D</Link>
                        <Link to='/departments' className={Componentcss.textwrapper3}>Departments</Link>
                        <Link to='/contactus' className={Componentcss.textwrapper4}>Contact Us</Link>
                    </div>
                    <Link to='/admin_login'><img className={Componentcss.element} src={image11} /></Link>
                    <Link to='/announcement'><img className={Componentcss.istockphoto} src={image3} /></Link>
                    <img className={Componentcss.pes} src={image4} />
                    <div className={Componentcss.textwrapper5}>PES UNIVERSITY HOSPITAL</div>
                    <img className={Componentcss.elementemergency} src={image2} />
                </div>
            </div>    
 )
}