import react from 'react';
import Menucss from './menuadmin.module.css';
import {Link} from 'react-router-dom';
// import image1 from './Patient.png';
import image2 from './Appoinment.png';
// import image3 from './Doctor.png';
// import image4 from './Pharmacy.png';
// import image5 from './LabTest.png';
import image6 from './Ambulance.png';
export default function Main(props) {
    return(
        

        <div className={Menucss.desktop}>
            <div className={Menucss.div}>
                {/* <Link to='/patient'><img className={Menucss.ellipse} src={image1} /></Link> */}
                
                <Link to='/consultation_admin'><img className={Menucss.ellipse2} src={image2} /></Link>
                {/* <Link to='/pharmacy'><img className={Menucss.istockphoto} src={image4} /></Link> */}
                <div className={Menucss.textwrapper4}>Consultation</div>
                <Link to='/Ambulance_admin'><img className={Menucss.element} src={image6} /></Link>
                <div className={Menucss.textwrapper6}>Ambulance</div>
            </div>
        </div>


    )
}