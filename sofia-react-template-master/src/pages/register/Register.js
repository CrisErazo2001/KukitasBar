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
import Widget from "../../components/Widget/Widget.js";
import Footer from "../../components/Footer/Footer.js";

// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";


const Register = (props) => {
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };
  const [state, setState] = useState({ username: '', password: '', admin: false} )

  const changeCred = (event) => {
    setState({ ...state, [event.target.name]: String(event.target.value) })
  }
  const [registerValue, setRegisterValue] = useState({});
  const doRegister = (event) => {
      event.preventDefault();
      console.log(state);

      if (state.password.length < 5) {
          toast(
              <Notification 
                  type={'warning'} 
                  errorMessage={'La contraseña debe ser de más de 5 caracteres'} 
                  withIcon 
              />, 
              options
          );
      } else {
          fetch('/register', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(state)
          })
          .then(response => response.json())
          .then(data => {
              setRegisterValue(data); // Guarda la respuesta en registerValue
          })
          .catch(error => console.error('Error:', error));
      }

      // Vacía los inputs del formulario
      setState({ username: '', password: '', admin: false });
      setChecked(false);
  };

  // Monitorea cambios en registerValue, muestra su valor en la consola e indica si han existido errores al crear usuarios
  useEffect(() => {
      console.log("RegisterValue (useEffect):", registerValue);
      if (registerValue.code === 200){
        toast(
          <Notification 
              type={'success'} 
              errorMessage={'Usuario Creado Correctamente'} 
              withIcon 
          />, 
          options
        );
      }else if (registerValue.code === 400){
        toast(
          
          <Notification 
              type={'error'} 
              errorMessage={registerValue.message} 
              withIcon 
          />, 
          options
        );
      }
      
  }, [registerValue]);

  const [checked, setChecked] = useState(false);

  const handleChange = () => {
    setChecked(!checked);
    setState({username: state.username, password: state.password,admin: !checked})
  }

  const { from } = props.location.state || { from: { pathname: '/template' } }

  {/*

  if (hasToken(JSON.parse(localStorage.getItem('authenticated')))) {
    return (
      <Redirect to={from} />
    );
  }
   */}

  return (
    <div className="auth-page">
      <Container className="col-1">
        <Row className="d-flex align-items-center">
          <Col xs={12} lg={6} className="left-column">
            <Widget className="widget-auth widget-p-lg">

              <div className="text-center py-3">
                {/* Título KUKITAS, centrado */}
                <p className="auth-header mb-0" style={{ fontSize: '3rem' }}>KUKITA'S</p>

                {/* Login, alineado a la derecha */}
                <div className="d-flex justify-content-end">
                  <p className="auth-header mb-0" style={{ marginRight: '0', marginTop: '10px' }}>Register</p>
                </div>
              </div>

              <form onSubmit={(event) => doRegister(event)}>

                
                <FormGroup className="my-3">

                <FormText>Username</FormText>
                  <Input
                    id="username"
                    className="input-transparent pl-3"
                    value={state.username}  
                    onChange={(event) => changeCred(event)}
                    type="text" 
                    required
                    name="username"
                    placeholder="Username" 
                  />
                </FormGroup>

                <FormGroup  className="my-3">
                  <div className="d-flex justify-content-between">
                    <FormText>Password</FormText>
                    
                    {/* 
                    <Link to="/error">Forgot password?</Link>
                    */}
                  </div>
                  <Input
                    id="password"
                    className="input-transparent pl-3"
                    value={state.password}
                    onChange={(event) => changeCred(event)}
                    type="password"
                    required
                    name="password"
                    placeholder="Password"
                  />
                </FormGroup>

                <div>
                  <label>
                    <input
                      type="checkbox"
                      checked={checked}
                      onChange={handleChange}
                    />
                  Admin
                  </label>

                  <p>This user will be "Admin"? {checked.toString()}</p>
                </div>

                <div className="bg-widget d-flex justify-content-center">
                  <Button className="button-log my-3" type="submit" color="secondary-red">Create new User</Button>
                </div>
                <p className="dividing-line my-1">&#8195;</p>
    
                <Link to="/login">Cancel</Link>
              </form>
            </Widget>
          </Col>

          {/*
          <Col xs={0} lg={6} className="right-column">
            <div>
              <img src={loginImage} alt="Error page" />
            </div>
          </Col>
           */}
        </Row>
      </Container>
    </div>
  )
}

Register.propTypes = {
  dispatch: PropTypes.func.isRequired,
}

function mapStateToProps(state) {
  return {
    isFetching: state.auth.isFetching,
    isAuthenticated: state.auth.isAuthenticated,
    errorMessage: state.auth.errorMessage,
  };
}

export default withRouter(connect(mapStateToProps)(Register));
