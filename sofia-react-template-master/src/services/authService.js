import mockUsers from "../mockUsers";

const hasToken = () => {
  return localStorage.getItem("authenticated") ? true : false;
};

export const loginUser = (auth,role) => {

  if (auth===200) {
    localStorage.setItem("authenticated", true);
    localStorage.setItem("role", role);
    return role; // Retorna el rol para pruebas
  } else {
    return null;
  }
};

export const logoutUser = () => {
  localStorage.removeItem("authenticated");
  localStorage.removeItem("role");
};

export const getUserRole = () => {
  return localStorage.getItem("role");
};

// Exporta `hasToken` como una exportación nombrada
export { hasToken };
