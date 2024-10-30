import React, { useState, useEffect } from "react";
import {
  Col,
  Row,
  Table,
  Pagination,
  PaginationItem,
  PaginationLink,
  Button,
  Input,
  InputGroup,
  InputGroupAddon
} from "reactstrap";
import { v4 as uuidv4 } from "uuid";
import * as XLSX from 'xlsx';
import searchIcon from "../../assets/tables/searchIcon.svg";
import printerIcon from "../../assets/tables/printerIcon.svg";
import s from "./Tables.module.scss";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";


const Tables = () => {
  const [deleteListStatus, setDeleteListStatus] = useState({});
  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };
  // Estado de la tabla
  const [listaPedidos, setListaPedidos] = useState([]);
  const [listaPedidosStatus, setListaPedidosStatus] = useState([]);


  const fetchPedidos = async () => {
    try {
      const response = await fetch('/pedidos'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched pedidos:', list.data); // Mostrar en consola la lista obtenida
      setListaPedidosStatus(list);
      setListaPedidos(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  


  const [busqueda, setBusqueda] = useState("");
  const [paginaActual, setPaginaActual] = useState(0);
  const tamanoPagina = 15;

  // Filtra la lista de pedidos según la búsqueda
  const pedidosFiltrados = listaPedidos.filter(pedido =>
    pedido.nombre_cliente.toLowerCase().includes(busqueda.toLowerCase())
  );

  // Elimina un pedido de la lista
  const eliminarPedido = (pedido) => {
    fetch('/pedido/eliminar', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(pedido)
    })
    .then(response => {
        console.log('Respuesta del servidor:', response); // Log de la respuesta
        return response.json();
    })
    .then(data => {
        console.log('Datos recibidos:', data); // Log de los datos recibidos
        setDeleteListStatus(data); // Guarda la respuesta en createIngStatus
        // setIngredientes((prevIngredientes) => [...prevIngredientes, nuevoIngrediente]);
    })
    .catch(error => console.error('Error:', error));
  };

  // Función para exportar a Excel
  const exportarExcel = () => {
    const hoja = XLSX.utils.json_to_sheet(pedidosFiltrados);
    const libro = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(libro, hoja, "Pedidos");
    XLSX.writeFile(libro, "Pedidos.xlsx");
  };

  // Control de la paginación
  const cantidadPaginas = Math.ceil(pedidosFiltrados.length / tamanoPagina);
  const cambiarPagina = (e, index) => {
    e.preventDefault();
    setPaginaActual(index);
  };

  useEffect(() => {
    fetchPedidos();
    
    if (deleteListStatus.code > 0 ){
      console.log('Estado de deleteListStatus:', deleteListStatus);
      toast(  
        <Notification 
            type={deleteListStatus.status} 
            errorMessage={deleteListStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [deleteListStatus]);

  useEffect(() => {
    if (listaPedidosStatus.code > 200 ){
      console.log('Estado de listaPedidosStatus:', listaPedidosStatus);
      toast(  
        <Notification 
            type={listaPedidosStatus.status} 
            errorMessage={listaPedidosStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [deleteListStatus]);
  

  return (
    <div>
      <Row>
        <Col>
          <Row className="mb-4">
            <Col>
              <div className={s.tableTitle}>
                <div className="headline-2">Tabla de pedidos</div>
                <div className="d-flex align-items-center">
                  <div className={s.searchContainer}> 
                 
                    <InputGroup className="input-group-no-border search-input-group">
                      <Input
                        type="text"
                        placeholder="Buscar Cliente"
                        value={busqueda}
                        onChange={(e) => setBusqueda(e.target.value)}
                        className={s.searchInput}
                      />
                      <InputGroupAddon addonType="prepend">
                        <span className={s.searchIcon}>
                          <img src={searchIcon} alt="Buscar" />
                        </span>
                      </InputGroupAddon>
                    </InputGroup>
                  </div>

                  <button className={s.print} onClick={exportarExcel}>
                    <img src={printerIcon} alt="Imprimir" />
                  </button>
                </div>
              </div>
              <Table responsive striped className="table-borderless table-hover">
                <thead>
                  <tr>
                    <th>Cliente</th>
                    <th>Bebida</th>
                    <th>Hora de Pedido</th>
                    <th>Hora de Entrega</th>
                    <th>Acción</th>
                  </tr>
                </thead>
                <tbody>
                  {pedidosFiltrados
                    .slice(paginaActual * tamanoPagina, (paginaActual + 1) * tamanoPagina)
                    .map((pedido) => (
                      <tr key={pedido.id_pedido}>
                        <td>{pedido.nombre_cliente}</td>
                        <td>{pedido.id_bebida}</td>
                        <td>{pedido.create_at}</td>
                        <td>{pedido.deliver_at}</td>
                        <td>
                          <Button
                            className={s.nBotonEdicion}
                            onClick={() => eliminarPedido(pedido)}
                          >
                            Eliminar
                          </Button>
                        </td>
                      </tr>
                    ))}
                </tbody>
              </Table>

              <Pagination className="pagination-borderless">
                <PaginationItem disabled={paginaActual <= 0}>
                  <PaginationLink
                    onClick={(e) => cambiarPagina(e, paginaActual - 1)}
                    previous
                    href="#top"
                  />
                </PaginationItem>
                {[...Array(cantidadPaginas)].map((_, i) => (
                  <PaginationItem active={i === paginaActual} key={i}>
                    <PaginationLink onClick={(e) => cambiarPagina(e, i)} href="#top">
                      {i + 1}
                    </PaginationLink>
                  </PaginationItem>
                ))}
                <PaginationItem disabled={paginaActual >= cantidadPaginas - 1}>
                  <PaginationLink
                    onClick={(e) => cambiarPagina(e, paginaActual + 1)}
                    next
                    href="#top"
                  />
                </PaginationItem>
              </Pagination>
            </Col>
          </Row>
        </Col>
      </Row>
    </div>
  );
};

export default Tables;
