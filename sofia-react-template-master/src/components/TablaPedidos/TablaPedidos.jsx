const TablaPedidos = ({ listaPedidos, eliminarPedido }) => {
    const handleEliminar = (id_pedidos) => {
      eliminarPedido(id_pedidos); // Función para manejar la eliminación de pedidos
    };
  
    return (
      <div className="tab-content">
        <h5 className="card-title fw-semibold mb-4">Pedidos Pendientes a entrega</h5>
        <table className="tabla-pedidos">
          <thead>
            <tr>
              <th><h6 className="fw-semibold mb-0">Nombre del Cliente</h6></th>
              <th><h6 className="fw-semibold mb-0">Solicitado</h6></th>
              <th><h6 className="fw-semibold mb-0">Bebida</h6></th>
              <th><h6 className="fw-semibold mb-0">Acción</h6></th>
            </tr>
          </thead>
          <tbody>
            {listaPedidos.map((item) => (
              <tr key={item.id_pedidos}>
                <td><h6 className="fw-semibold mb-1">{item.nombre_cliente}</h6></td>
                <td><p className="mb-0 fw-normal">{item.create_at}</p></td>
                <td><p className="mb-0 fw-normal">{item.id_receta}</p></td>
                <td>
                  <button
                    type="button"
                    onClick={() => handleEliminar(item.id_pedidos)}
                    className="btn btn-outline-primary"
                  >
                    Eliminar Pedido
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };
  // Exportación por defecto
export default TablaPedidos;