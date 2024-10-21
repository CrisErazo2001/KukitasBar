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
import Widget from "../../components/Widget/Widget.js";
import Footer from "../../components/Footer/Footer.js";

import loginImage from "../../assets/registerImage.svg";
import SofiaLogo from "../../components/Icons/SofiaLogo.js";
import GoogleIcon from "../../components/Icons/AuthIcons/GoogleIcon.js";
import TwitterIcon from "../../components/Icons/AuthIcons/TwitterIcon.js";
import FacebookIcon from "../../components/Icons/AuthIcons/FacebookIcon.js";
import GithubIcon from "../../components/Icons/AuthIcons/GithubIcon.js";
import LinkedinIcon from "../../components/Icons/AuthIcons/LinkedinIcon.js";
import { registerUser } from "../../actions/register.js";
import hasToken from "../../services/authService";

const Register = (props) => {
  const [state, setState] = useState({ email: '', password: ''} )

  const changeCred = (event) => {
    setState({ ...state, [event.target.name]: event.target.value })
  }

  const doRegister = (event) => {
    event.preventDefault();
    props.dispatch(registerUser({
      creds: state,
      history: props.history,
    }))
  }

  const [checked, setChecked] = React.useState(false);

  const handleChange = () => {
    setChecked(!checked);
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

                  <p>Is "Admin" checked? {checked.toString()}</p>
                </div>

                <div className="bg-widget d-flex justify-content-center">
                  <Button className="button-log my-3" type="submit" color="secondary-red">Sign Up</Button>
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
      <Footer />
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
