import React from "react";
import FooterIcon from "../Icons/FooterIcon";
import s from "./Footer.module.scss";
import gifKukitas from "./Batiendo.gif"


const Footer = () => {
  return (
    <div className={s.footTotal}>
      
      <div className={s.footer}>
        <span className={s.footerLabel}>2024 KUKITA`s  </span>
        <img src={gifKukitas} style={{width:"75px"}}></img>
      </div>
    </div>
  )
}

export default Footer;
