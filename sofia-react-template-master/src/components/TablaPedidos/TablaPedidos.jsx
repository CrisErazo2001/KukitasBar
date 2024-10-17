import s from "../../pages/tables/Tables.module.scss";

const TablaPedidos = ({ listaPedidos, eliminarPedido }) => {
    const handleEliminar = (id_pedidos) => {
      eliminarPedido(id_pedidos); // Función para manejar la eliminación de pedidos
    };
  
    return (
      <div className="tab-content">
        <h5 className="card-title fw-semibold mb-4">Pedidos Pendientes a entrega</h5>
        {/* 
        <table className="tabla-pedidos">
        */}
        <table className="table-striped table-borderless " responsive>
          <thead>
            <tr>
              {/*
              <th><h6 className="fw-semibold mb-0 w-25">Nombre del Cliente</h6></th>
              <th><h6 className="fw-semibold mb-0 w-25">Fecha Solicitado</h6></th>
              <th><h6 className="fw-semibold mb-0 w-25">Bebida</h6></th>
              <th><h6 className="fw-semibold mb-0 w-25">Modificar</h6></th>
               */}
              <th className="fw-semibold mb-0 w-25">Nombre del Cliente</th>
              <th className="fw-semibold mb-0 w-25">Fecha Solicitado</th>
              <th className="fw-semibold mb-0 w-25">Bebida</th>
              <th className="fw-semibold mb-0 w-25">Modificar</th>


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
                    className="btn btn-outline-danger"
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