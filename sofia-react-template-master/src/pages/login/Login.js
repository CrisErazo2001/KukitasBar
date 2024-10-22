import React, { useState } from "react";
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
import Widget from "../../components/Widget/Widget";
import Footer from "../../components/Footer/Footer";
import { loginUser } from "../../actions/auth";
import hasToken from "../../services/authService";

import loginImage from "../../assets/loginImage.svg";
import robotSaluda from "../../assets/Saludo.gif"

const Login = (props) => {

  const [state, setState] = useState({
    email: 'admin@flatlogic.com',
    password: 'password',
  })

  const doLogin = (e) => {
    e.preventDefault();
    props.dispatch(loginUser({ password: state.password, email: state.email }))
  }

  const changeCreds = (event) => {
    setState({ ...state, [event.target.name]: event.target.value })
  }

  const { from } = props.location.state || { from: { pathname: '/template' }};
  if (hasToken(JSON.parse(localStorage.getItem('authenticated')))) {
    return (
      <Redirect to={from} />
    )
  }

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
                  <p className="auth-header mb-0" style={{ marginRight: '0', marginTop: '10px' }}>Login</p>
                </div>
              </div>

              <form onSubmit={(event) => doLogin(event)}>

                {/*
                <FormGroup className="my-3">
                  <FormText>Email</FormText>
                  <Input
                    id="email"
                    className="input-transparent pl-3"
                    value={state.email}
                    onChange={(event) => changeCreds(event)}
                    type="email"
                    required
                    name="email"
                    placeholder="Email"
                  />
                </FormGroup>
                */}
                <FormGroup className="my-3">

                <FormText>Username</FormText>
                  <Input
                    id="username"
                    className="input-transparent pl-3"
                    value={state.username}  
                    onChange={(event) => changeCreds(event)}
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
                    onChange={(event) => changeCreds(event)}
                    type="password"
                    required
                    name="password"
                    placeholder="Password"
                  />
                </FormGroup>

                <div className="bg-widget d-flex justify-content-center">
                  <Button className="button-log my-3" type="submit" color="secondary-red">Login</Button>
                </div>
                <p className="dividing-line my-3">&#8195;&#8195;</p>
                <div className="bg-widget d-flex justify-content-center flex-column align-items-center my-7">
                  <Button className="button-log my-2" type="submit" color="secondary-red">Menú Principal</Button>
                  <Button className="button-log my-1" type="submit" color="secondary-red">Listado de Bebidas</Button>
                </div>
                
                {/*
                <Link to="/register">Don’t have an account? Sign Up here</Link>
                */}
                </form>
            </Widget>
          </Col>
          {/*
          <Col xs={1} lg={2} className="right-column">
            <div>
              <img src={robotSaluda} alt="Error page" />
            </div>
          </Col>
          */}
        </Row>
      </Container>
      <Footer />
    </div>
  )
}


Login.propTypes = {
  dispatch: PropTypes.func.isRequired,
}

function mapStateToProps(state) {
  return {
    isFetching: state.auth.isFetching,
    isAuthenticated: state.auth.isAuthenticated,
    errorMessage: state.auth.errorMessage,
  };
}

export default withRouter(connect(mapStateToProps)(Login));
