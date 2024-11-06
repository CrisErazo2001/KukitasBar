import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import { withRouter, Redirect, Link } from "react-router-dom";
import { connect } from "react-redux";
import {
  Container,
  Row,
  Col,
  Button,
  FormGroup,
  FormText,
  Input,
} from "reactstrap";
import { loginUser } from "../../services/authService";
import { hasToken } from "../../services/authService";


import Widget from "../../components/Widget/Widget";
import Footer from "../../components/Footer/Footer";
//import { loginUser, hasToken, getUserRole } from "../../services/authService";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";


const Login = (props) => {
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };
  const [userStatus, setUserStatus] = useState({});
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [redirectTo, setRedirectTo] = useState(null);  // Nueva variable para gestionar la redirección

  const doLogin = (e) => {
    e.preventDefault();
    // const role = loginUser(username, password);  
    fetch('/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({username: username, password:password})
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); 
        setUserStatus(data); 
        
    })
    .catch(error => console.error('Error:', error));
    
  };

  useEffect(() => {
    
    
    if (userStatus.code == 200){
      console.log('userStauts',userStatus.code);
      const role = loginUser(userStatus.code, userStatus.redirect);
      // Si el usuario es autenticado, definimos la redirección
      setRedirectTo(role === "admin" ? "/template/tables" : "/template/tables");
      setRedirectTo(role === "operator" ? "/template/tables" : "/template/tables");
    } 
    if (userStatus.code > 0){
      
      toast(
        
        <Notification 
            type={userStatus.status} 
            errorMessage={userStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
    
    
  }, [userStatus]);

  if (hasToken() || redirectTo) {
    return <Redirect to={redirectTo || "/template"} />;
  }
  
  // Redireccionar si ya está autenticado o si el usuario se logueó
  
  return (
    <div className="auth-page">
      <Container className="col-1">
        <Row className="d-flex align-items-center">
          <Col xs={12} lg={6} className="left-column">
            <Widget className="widget-auth widget-p-lg">
              <div className="text-center py-3">
                <p className="auth-header mb-0" style={{ fontSize: "3rem" }}>KUKITA'S</p>
                <div className="d-flex justify-content-end">
                  <p className="auth-header mb-0" style={{ marginRight: "0", marginTop: "10px" }}>Login</p>
                </div>
              </div>
              <form onSubmit={doLogin}>
                <FormGroup className="my-3">
                  <FormText>Username</FormText>
                  <Input
                    id="username"
                    className="input-transparent pl-3"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    type="text"
                    required
                    name="username"
                    placeholder="Username"
                  />
                </FormGroup>
                <FormGroup className="my-3">
                  <FormText>Password</FormText>
                  <Input
                    id="password"
                    className="input-transparent pl-3"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    type="password"
                    required
                    name="password"
                    placeholder="Password"
                  />
                </FormGroup>
                <div className="bg-widget d-flex justify-content-center">
                  <Button className="button-log my-3" type="submit" color="secondary-red">
                    Login
                  </Button>
                </div>
              </form>
              <p className="dividing-line my-3">&#8195; ir a &#8195;</p>
                <div className="bg-widget d-flex justify-content-center flex-column align-items-center my-7">
                  {/*<Button className="button-log my-2 d-flex justify-content-center align-items-center" href ='http://192.168.0.226:5000http://127.0.0.1:5000' color="secondary-red">Menú Principal</Button>
                  */}
                  <Button className="button-log my-2 d-flex justify-content-center align-items-center" href ='http://192.168.0.241:5000' color="secondary-red">Menú Principal</Button>
                  {/*<Button className="button-log my-1 d-flex justify-content-center align-items-center" href ='http://127.0.0.1:5000/lista-pedidos http://192.168.0.226:5000/lista-pedidos' color="secondary-red">Listado de Bebidas</Button>
                  */}
                  <Button className="button-log my-1 d-flex justify-content-center align-items-center" href ='http://192.168.0.241:5000/lista-pedidos' color="secondary-red">Listado de Bebidas</Button>
                </div>
            </Widget>
          </Col>
        </Row>
      </Container>
      <Footer />
    </div>
  );
};

Login.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

export default withRouter(Login);




















