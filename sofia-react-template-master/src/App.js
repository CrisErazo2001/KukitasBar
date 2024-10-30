// -- React and related libs
import React, { useEffect } from "react";
import { Switch, Route, Redirect } from "react-router";
import { HashRouter } from "react-router-dom";
import PrivateRoute from "./components/PrivateRoute/PrivateRoute";

// -- Redux
import { connect } from "react-redux";

// -- Custom Components
import LayoutComponent from "./components/Layout/Layout";
import ErrorPage from "./pages/error/ErrorPage";

import Noautorizado from "./pages/noautorizado/Noautorizado";
import Login from "./pages/login/Login";
import Register from "./pages/register/Register";

// -- Redux Actions Ya no hace falta
import { logoutUser } from "./actions/auth";

// -- Third Party Libs
import { ToastContainer } from "react-toastify";

// -- Services
import isAuthenticated from "./services/authService";

// -- Component Styles
import "./styles/app.scss";

{/*
const PrivateRoute = ({ dispatch, component, ...rest }) => {
  // Verificar si el usuario está autenticado
  if (!isAuthenticated(JSON.parse(localStorage.getItem("authenticated")))) {
    dispatch(logoutUser());
    return (<Redirect to="/login" />)
  } else {
    return (
      <Route { ...rest } render={props => (React.createElement(component, props))} />
    );
  }
};
 */}

const App = (props) => {
  // Borrar autenticación al iniciar la aplicación
  useEffect(() => {
    localStorage.removeItem("authenticated");
  }, []);

  return (
    <div>
      <ToastContainer />
      <HashRouter>
        <Switch>

          
          {/* Redirigir siempre al login si no está autenticado */}
          
          <Route path="/" exact render={() => <Redirect to="/login" />} />
          
          <Route path="/template" exact render={() => <Redirect to="/template/tables" />} />
          
          
          {/* Ruta privada que requiere autenticación */}
          
          <PrivateRoute path="/template" dispatch={props.dispatch} component={LayoutComponent} />
          
          {/* Ruta de Login */}
          
          <Route path="/login" exact component={Login} />
          
          


          {/*
          <Route path="/" exact render={() => <Redirect to="/login" />} />
          <Route path="/login" exact component={Login} />
             */}
          {/* Rutas protegidas con acceso basado en roles */}

          {/*
          <PrivateRoute path="/template" exact render={() => <Redirect to="/template/tables" />} />
          
  
          <PrivateRoute path="/template/register" requiredRole="admin" component={Register} />
          */}
          {/* Rutas accesibles para todos los roles */}


          
          {/* Rutas adicionales */}
          <Route path="/error" exact component={ErrorPage} />
          
          {/* Ruta común para acceso no autorizado */}
          <Route path="/unauthorized" exact component={Noautorizado} />
          
          {/* Ruta por defecto para páginas no encontradas */}
          <Route component={ErrorPage} />
          <Route path="*" exact render={() => <Redirect to="/error" />} />
        </Switch>
      </HashRouter>
    </div>
  );
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps)(App);
