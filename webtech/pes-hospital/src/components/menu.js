import react from 'react';
import Menucss from './menu.module.css';
import {Link} from 'react-router-dom';
// import image1 from './Patient.png';
import image2 from './Appoinment.png';
import image3 from './Doctor.png';
// import image4 from './Pharmacy.png';
// import image5 from './LabTest.png';
import image6 from './Ambulance.png';
export default function Main(props) {
    return(
        

        <div className={Menucss.desktop}>
            <div className={Menucss.div}>
                {/* <Link to='/patient'><img className={Menucss.ellipse} src={image1} /></Link> */}
                <div className={Menucss.overlapgroup}>
                <Link to="./Doctor_detail"><img className={Menucss.img} src={image3} /></Link>
                    <div className={Menucss.textwrapper}>Doctor</div>
                </div>
                <Link to='/consultation'><img className={Menucss.ellipse2} src={image2} /></Link>
                {/* <div className={Menucss.textwrapper2}>Patient</div> */}
                {/* <div className={Menucss.textwrapper3}>Pharmacy</div> */}
                {/* <Link to='/pharmacy'><img className={Menucss.istockphoto} src={image4} /></Link> */}
                <div className={Menucss.textwrapper4}>Consultation</div>
                {/* <Link to='/labtest'><img className={Menucss.chemicallabtest} src={image5}/></Link> */}
                {/* <div className={Menucss.textwrapper5}>Lab Test</div> */}
                <Link to='/Ambulance'><img className={Menucss.element} src={image6} /></Link>
                <div className={Menucss.textwrapper6}>Ambulance</div>
            </div>
        </div>


    )
}