// -- React and related libs
import React from "react";
import { Switch, Route, Redirect } from "react-router";
import { HashRouter } from "react-router-dom";

// -- Redux
import { connect } from "react-redux";

// -- Custom Components
import LayoutComponent from "./components/Layout/Layout";
import ErrorPage from "./pages/error/ErrorPage";
import Login from "./pages/login/Login";
import Register from "./pages/register/Register";

// -- Redux Actions
import { logoutUser } from "./actions/auth";

// -- Third Party Libs
import { ToastContainer } from "react-toastify";

// -- Services
import isAuthenticated from "./services/authService";

// -- Component Styles
import "./styles/app.scss";

// PrivateRoute component to guard routes that require authentication
const PrivateRoute = ({ dispatch, component, ...rest }) => {
  if (!isAuthenticated(JSON.parse(localStorage.getItem("authenticated")))) {
    dispatch(logoutUser()); // Logout if not authenticated
    return <Redirect to="/login" />;
  }
  return <Route {...rest} render={props => React.createElement(component, props)} />;
};

const App = (props) => {
  return (
    <div>
      <ToastContainer />
      <HashRouter>
        <Switch>
          {/* Redirect root path to login */}
          <Route path="/" exact render={() => <Redirect to="/login" />} />

          {/* Public routes */}
          <Route path="/login" exact component={Login} />
          <Route path="/error" exact component={ErrorPage} />

          {/* Private routes */}
          <PrivateRoute path="/template" dispatch={props.dispatch} component={LayoutComponent} />

          {/* Catch-all route for undefined paths */}
          <Route component={ErrorPage} />
        </Switch>
      </HashRouter>
    </div>
  );
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps)(App);

