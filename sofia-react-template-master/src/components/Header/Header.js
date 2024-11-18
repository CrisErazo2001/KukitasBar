import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import { withRouter } from "react-router";
import { connect } from "react-redux";

import {
  Navbar,
  Nav,
  NavItem,
  NavLink,
  InputGroupAddon,
  InputGroup,
  Input,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  Button,
  DropdownItem,
  Form,
  FormGroup,
  Alert,
} from "reactstrap";

import { logoutUser } from "../../actions/auth";
import { closeSidebar, openSidebar } from "../../actions/navigation";
import MenuIcon from "../Icons/HeaderIcons/MenuIcon";
import SearchBarIcon from "../Icons/HeaderIcons/SearchBarIcon";
import SearchIcon from "../Icons/HeaderIcons/SearchIcon";

import ProfileIcon from "../../assets/navbarMenus/pfofileIcons/ProfileIcon";
import MessagesIcon from "../../assets/navbarMenus/pfofileIcons/MessagesIcon";
import TasksIcon from "../../assets/navbarMenus/pfofileIcons/TasksIcon";

import logoutIcon from "../../assets/navbarMenus/pfofileIcons/logoutOutlined.svg";
import basketIcon from "../../assets/navbarMenus/basketIcon.svg";
import calendarIcon from "../../assets/navbarMenus/calendarIcon.svg";
import envelopeIcon from "../../assets/navbarMenus/envelopeIcon.svg";
import mariaImage from "../../assets/navbarMenus/mariaImage.jpg";
import notificationImage from "../../assets/navbarMenus/notificationImage.jpg";
import userImg from "../../assets/user.svg";

import s from "./Header.module.scss";
import "animate.css";

const Header = (props) => {
  
  const [menuOpen, setMenuOpen] = useState(false);
  const [notificationsOpen, setNotificationsOpen] = useState(false);
  const [user, setUser] = useState({user:''});

  // WebSocket States
  const [showManualAddButton, setShowManualAddButton] = useState(false); // To control visibility of the button
  const [showRetirarMessage, setShowRetirarMessage] = useState(false); // To control "Retirar Vaso" message visibility
  const [showParoMessage, setShowParoMessage] = useState(false); // To control "Retirar Vaso" message visibility
  const [showParoEMessage, setShowParoEMessage] = useState(false); // To control "Retirar Vaso" message visibility
  const [showParoFMessage, setShowParoFMessage] = useState(false); // To control "Retirar Vaso" message visibility
  const [wsError, setWsError] = useState(null); // WebSocket for errorbotella
  const [wsReconocer, setWsReconocer] = useState(null); // WebSocket for reconocervaso
  const [wsRetirar, setWsRetirar] = useState(null); // WebSocket for retirarvaso
  const [wsParo, setWsParo] = useState(null); // WebSocket for paro Robots
  const [wsParoE, setWsParoE] = useState(null); // WebSocket for paro Robots
  const [wsParoF, setWsParoF] = useState(null); // WebSocket for paro Robots
  

  

  const fetchData = async () => {
    try {
      const response = await fetch('/user', {
        method: 'GET', // or 'POST' depending on your use case
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await response.json();
      
      setUser(result); // Use setData to update the state
      return result; // Return the result if needed elsewhere
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };
  console.log('Fetched User:', user); // Log the data
  useEffect(() => {
    fetchData();
  }, []);

    // Initialize WebSockets on mount
    useEffect(() => {
      const wserror = new WebSocket("ws://192.168.0.241:1880/ws/errorbotella");
      const wsreconocer = new WebSocket("ws://192.168.0.241:1880/ws/reconocervaso");
      const wsretirar = new WebSocket("ws://192.168.0.241:1880/ws/retirarvaso");
      const wsparo = new WebSocket("ws://192.168.0.241:1880/ws/stoprobots");
      const wsparoe = new WebSocket("ws://192.168.0.241:1880/ws/paroexterno");
      const wsparof = new WebSocket("ws://192.168.0.241:1880/ws/robotsfallo");
  
      setWsError(wserror);
      setWsReconocer(wsreconocer);
      setWsRetirar(wsretirar);
      setWsParo(wsparo);
      setWsParoE(wsparoe);
      setWsParoF(wsparof);
  
      // Listener for wsError
      wserror.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log("Received from wserror:", data);
          if (data === true) {
            setShowManualAddButton(true); // Show button if error is true
          } else {
            setShowManualAddButton(false);
          }
        } catch (e) {
          console.error("Error parsing WebSocket message:", e);
        }
      };
      // Listener for wsRetirar
      wsretirar.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log("Received from wsretirar:", data);
          setShowRetirarMessage(data === true); // Show "Retirar Vaso" message if true
        } catch (e) {
          console.error("Error parsing WebSocket message:", e);
        }
      };
      // Listener for wsParo
      wsparo.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log("Received from wsparo:", data);
          setShowParoMessage(data === true); // Show "Retirar Vaso" message if true
        } catch (e) {
          console.error("Error parsing WebSocket message:", e);
        }
      };
      // Listener for wsParo
      wsparoe.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log("Received from wsparo:", data);
          setShowParoEMessage(data === false); // Show "Retirar Vaso" message if true
        } catch (e) {
          console.error("Error parsing WebSocket message:", e);
        }
      };
      // Listener for wsParo
      wsparof.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log("Received from wsparo:", data);
          setShowParoFMessage(data === false); // Show "Retirar Vaso" message if true
        } catch (e) {
          console.error("Error parsing WebSocket message:", e);
        }
      };
  
      // Cleanup WebSocket connections on component unmount
      return () => {
        wserror.close();
        wsreconocer.close();
        wsretirar.close();
        wsparo.close();
        wsparoe.close();
        wsparof.close();
      };
    }, []);
  
    // Handle manual glass addition
    const handleManualAdd = () => {
      if (wsReconocer && wsReconocer.readyState === WebSocket.OPEN) {
        // Envía "true"
        wsReconocer.send(JSON.stringify(true));
        console.log("Sent true to wsreconocer");
    
        // Espera 1 segundo y envía "false"
        setTimeout(() => {
          if (wsReconocer && wsReconocer.readyState === WebSocket.OPEN) {
            wsReconocer.send(JSON.stringify(false));
            console.log("Sent false to wsreconocer");
          }
          wsReconocer.send(JSON.stringify(false));
        }, 1000);
      } else {
        console.error("WebSocket for reconocervaso is not open");
      }
    };
    

  const toggleNotifications = () => {
    setNotificationsOpen(!notificationsOpen);
  }

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  }

  const toggleSidebar = () => {
    if (props.sidebarOpened) {
      props.dispatch(closeSidebar());
    } else {
      const paths = props.location.pathname.split('/');
      paths.pop();
      props.dispatch(openSidebar());
    }
  }

  const doLogout = () => {
    props.dispatch(logoutUser());
  }



  return (
    <Navbar className={`${s.root} d-print-none`}>
      <div>
        <NavLink
          onClick={() => toggleSidebar()}
          className={`d-md-none mr-3 ${s.navItem}`}
          href="#"
        >
          <MenuIcon className={s.menuIcon} />
        </NavLink>
        
      </div>
      
      {/*
      <Form className="d-none d-sm-block" inline>
        <FormGroup>
          <InputGroup className='input-group-no-border'>
            <Input id="search-input" placeholder="Search Dashboard" className='focus'/>
            <InputGroupAddon addonType="prepend">
              <span>
                <SearchBarIcon/>
              </span>
            </InputGroupAddon>
          </InputGroup>
        </FormGroup>
      </Form>
       */}
      {/* Manual Add Button */}
      {showManualAddButton && (
        <Button
          className={s.nBotonRecetas}
          onClick={handleManualAdd}
        >
          Se Agregó un Vaso Manualmente
        </Button>
      )}

      {/* Retirar Vaso Message */}
      {showParoMessage && (
        <p  className={s.quitarvaso}>
          ¡ Alerta Los Robots se han Pausado !
        </p>
      )}
      {/* Retirar Vaso Message */}
      {showRetirarMessage && (
        <p  className={s.quitarvaso}>
          ¡ Alerta Retirar Vaso !
        </p>
      )}
      {/* Retirar Vaso Message */}
      {showParoEMessage && (
        <p  className={s.quitarvaso}>
          ¡ Alerta Paro Externo de Emergencia !
        </p>
      )}
      {/* Retirar Vaso Message */}
      {showParoFMessage && (
        <p  className={s.quitarvaso}>
          ¡ Alerta Los Robots Están en Fallo !
        </p>
      )}

      <Nav className="ml-auto">
        <NavItem className="d-sm-none mr-4">
          <NavLink
            className=""
            href="#"
          >
            
            <SearchIcon />
          </NavLink>
        </NavItem>


 
        <Dropdown isOpen={notificationsOpen} toggle={() => toggleNotifications()} nav id="basic-nav-dropdown" className="ml-3">
          <DropdownToggle nav caret className="navbar-dropdown-toggle">
            <span className={`${s.avatar} rounded-circle float-left mr-2`}>
              <img src={userImg} alt="User"/>
            </span>
            <span className="small d-none d-sm-block ml-1 mr-2 body-1">{user.user}</span>
          </DropdownToggle>
          <DropdownMenu className="navbar-dropdown profile-dropdown" style={{ width: "194px" } } right>
            {/*
            <DropdownItem className={s.dropdownProfileItem}><ProfileIcon/><span>Profile</span></DropdownItem>
            <DropdownItem className={s.dropdownProfileItem}><TasksIcon/><span>Tasks</span></DropdownItem>
            <DropdownItem className={s.dropdownProfileItem}><MessagesIcon/><span>Messages</span></DropdownItem>
             */}
            <NavItem>
              <NavLink onClick={() => doLogout()} href="#" >
                <button  className="btn btn-primary rounded-pill logout-btn"
                style={{
                  backgroundColor:'#f4431f',
                  width:'100%'


                }}
                
                type="submit"><img src={logoutIcon} alt="Logout"/><span className="ml-1">Logout</span></button>
              </NavLink>
            </NavItem>
          </DropdownMenu>
        </Dropdown>
      </Nav>
    </Navbar>
  )
}

Header.propTypes = {
  dispatch: PropTypes.func.isRequired,
  sidebarOpened: PropTypes.bool,
}

function mapStateToProps(store) {
  return {
    sidebarOpened: store.navigation.sidebarOpened,
    sidebarStatic: store.navigation.sidebarStatic,
  };
}

export default withRouter(connect(mapStateToProps)(Header));

