import mockUsers from "../mockUsers";

const hasToken = () => {
  return localStorage.getItem("authenticated") ? true : false;
};

export const loginUser = (username, password) => {
  const user = mockUsers.find(
    (user) => user.username === username && user.password === password
  );

  if (user) {
    localStorage.setItem("authenticated", true);
    localStorage.setItem("role", user.role);
    return user.role; // Retorna el rol para pruebas
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
