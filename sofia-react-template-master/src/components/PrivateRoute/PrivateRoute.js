// src/components/PrivateRoute/PrivateRoute.js
import React from "react";
import { Route, Redirect } from "react-router-dom";
import { getUserRole, hasToken } from "../../services/authService";


const PrivateRoute = ({ component: Component, requiredRole, ...rest }) => {
  const isAuthenticated = hasToken();
  const userRole = getUserRole();

  return (
    <Route
      {...rest}
      render={(props) =>
        isAuthenticated ? (
          requiredRole && userRole !== requiredRole ? (
            // Si el rol del usuario no coincide con el requerido, redirige a /unauthorized
            <Redirect to="/unauthorized" />
          ) : (
            // Si está autenticado y tiene el rol adecuado, renderiza el componente
            <Component {...props} />
          )
        ) : (
          // Si no está autenticado, redirige a /login
          <Redirect to="/login" />
        )
      }
    />
  );
};

export default PrivateRoute;

{/* 

// src/components/PrivateRoute.js
import React from "react";
import { Route, Redirect } from "react-router-dom";
import { connect } from "react-redux";
//import { isAuthenticated, getUserRole } from "../services/authService";
import { isAuthenticated, getUserRole } from "../../services/authService";
//import { logoutUser } from "../actions/auth"; // Asegúrate de importar la acción de logout
import { logoutUser } from "../../actions/auth";

const PrivateRoute = ({ component: Component, requiredRole, dispatch, ...rest }) => {
  const isAuth = isAuthenticated();
  const userRole = getUserRole();

  // Si el usuario no está autenticado, redirige al login y ejecuta logout
  if (!isAuth) {
    dispatch(logoutUser());
    return <Redirect to="/login" />;
  }

  // Si el rol no coincide, redirige a la página de "No autorizado"
  if (requiredRole && userRole !== requiredRole) {
    return <Redirect to="/unauthorized" />;
  }

  // Renderiza el componente si está autenticado y tiene el rol adecuado
  return <Route {...rest} render={(props) => <Component {...props} />} />;
};

export default connect()(PrivateRoute);

*/}
//Este componente recibe requiredRole como una propiedad para verificar el rol del usuario antes de renderizar la página.

