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
  InputGroupAddon,
  Modal,
  ModalBody
} from "reactstrap";

import ApexCharts from "react-apexcharts";


import BebidasPorDiaChart from "./BebidasPorDiaChart .js"; // Asegúrate de la ruta correcta
import dayjs from "dayjs";

//import { v4 as uuidv4 } from "uuid";
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
  const [busqueda, setBusqueda] = useState("");
  const [paginaActual, setPaginaActual] = useState(0);
  const [fechaInicio, setFechaInicio] = useState("");
  const [fechaFin, setFechaFin] = useState("");
  const tamanoPagina = 15;

  const fetchPedidos = async () => {
    try {
      const response = await fetch('/historial'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched historial:', list.data); // Mostrar en consola la lista obtenida
      setListaPedidosStatus(list);
      setListaPedidos(list.data); // Guardar la lista en el estado
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  // Filtra la lista de pedidos según la búsqueda y el rango de fechas
  const pedidosFiltrados = listaPedidos.filter((pedido) => {
    const readyAtDate = new Date(pedido.ready_at);
    const startDate = fechaInicio ? new Date(fechaInicio) : null;
    const endDate = fechaFin ? new Date(fechaFin) : null;
    const inDateRange = (!startDate || readyAtDate >= startDate) && (!endDate || readyAtDate <= endDate);
    const matchesSearch = pedido.nombre_receta.toLowerCase().includes(busqueda.toLowerCase());
    return matchesSearch && inDateRange;
  });

    /* nuevo modal */

    const [showConfirmModal, setShowConfirmModal] = useState(false); // Estado para mostrar el modal de confirmación
  
    /* Nuevo Modal*/
    // Mostrar el modal de confirmación
    const handleShowConfirmModal = () => {
      setShowConfirmModal(true);
    };
  
    // Ocultar el modal de confirmación
    const handleCloseConfirmModal = () => {
      setShowConfirmModal(false);
  
    };
  
      // Confirmar la eliminación
      const handleConfirmDelete = () => {
        eliminarPedido();
        handleCloseConfirmModal(); // Cerrar el modal después de la eliminación
      };
  
  
  
    /* nuevo modal */

  const eliminarPedido = async (pedido) => {
    try {
      const response = await fetch('/historial/eliminar'); // Reemplaza con tu URL de API
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const list = await response.json();
      console.log('Fetched historial delete:', list); // Mostrar en consola la lista obtenida
      setDeleteListStatus(list);
      
    } catch (error) {
      console.error('Fetch error:', error);
    }
    
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


  /* Nuevo */
  // Configuración para la gráfica de bebidas
  const conteoBebidas = pedidosFiltrados.reduce((acc, pedido) => {
    acc[pedido.nombre_receta] = (acc[pedido.nombre_receta] || 0) + 1;
    return acc;
  }, {});
  const bebidasSeries = Object.values(conteoBebidas);
  const bebidasLabels = Object.keys(conteoBebidas);
  // Array de colores que se aplicarán a las barras, puedes modificar los colores aquí
  const coloresBarras = ["#FF5733", "#31FF57", "#3357FF", "#FF33A1", "#FF8333", "#FF5733", "#33FFF5", "#5733FF"];

  const bebidasChartSettings = {
    chart: { 
      type: 'bar', 
      height: 300, 
      toolbar: { show: false } 
    },
    plotOptions: { 
      bar: { 
        borderRadius: 4, 
        horizontal: false, 
        colors: {
          ranges: bebidasLabels.map((_, index) => ({
            from: index,
            to: index,
            color: coloresBarras[index % coloresBarras.length], // Aplica un color diferente para cada barra
          }))
        }
      } 
    },
    xaxis: { 
      categories: bebidasLabels 
    }
  };

  // Configuración para la gráfica de ingredientes sin valores vacíos
  const conteoIngredientes = pedidosFiltrados.reduce((acc, pedido) => {
    pedido.ingredientes.split("-").forEach(ing => {
      const ingrediente = ing.trim();
      if (ingrediente) { // Evita valores vacíos
        acc[ingrediente] = (acc[ingrediente] || 0) + 1;
      }
    });
    return acc;
  }, {});
  const ingredientesSeries = Object.values(conteoIngredientes);
  const ingredientesLabels = Object.keys(conteoIngredientes);

  const ingredientesChartSettings = {
    chart: { type: 'pie', height: 300, toolbar: { show: false } },
    labels: ingredientesLabels
  };

  return (
    <div>
      <Row>
        <Col>
          <Row className="mb-4">
            <Col>
            
                <div className="mb-4" style={{ display:'flex', width:'100%',alignItems:'center', justifyContent:'space-between'}}>
                  <div className="headline-2">Historico de pedidos</div>
                  <div className={s.searchContainer}> 
                      <InputGroup className="input-group-no-border search-input-group">
                        <Input
                          type="text"
                          placeholder="Buscar Bebida"
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
                </div>
                <h5> Filtrar por fechas </h5>
                <div className="mb-4" style={{ display:'flex', width:'100%', height:'50px',alignItems:'center', justifyContent:'center'}}>
                  <div style={{display:'flex', flexDirection:'column', justifyContent:'center', alignItems:'center'}}>
                    <h7>Fecha Inicio</h7>
                    <Input
                      type="date"
                      placeholder="Fecha inicio"
                      value={fechaInicio}
                      onChange={(e) => setFechaInicio(e.target.value)}
                      className={`${s.dateInput} mr-3`}
                    />
                  </div>
                  <div style={{display:'flex', flexDirection:'column', justifyContent:'center', alignItems:'center'}}>
                    <h7>Fecha Fin</h7>
                    <Input
                      type="date"
                      placeholder="Fecha fin"
                      value={fechaFin}
                      onChange={(e) => setFechaFin(e.target.value)}
                      className={s.dateInput}
                    />
                  </div>

  
                </div>
                <div className="mb-4" style={{ display:'flex', width:'100%', height:'50px',alignItems:'center', justifyContent:'center'}}>
                  <button className={s.print} onClick={exportarExcel}>
                    <img src={printerIcon} alt="Imprimir" />
                  </button>
                </div>
            
              
              <Table responsive striped className="table-borderless table-hover">
                <thead>
                  <tr>
                    
                    <th>Bebida</th>
                    <th>Ingredientes</th>
                    <th>Hora de pedido</th>
                    <th>Hora de entrega</th>
                    <th>Hielo?</th>
                    <th>Costo Bebida</th>
                  </tr>
                </thead>
                <tbody>
                  {pedidosFiltrados
                    .slice(paginaActual * tamanoPagina, (paginaActual + 1) * tamanoPagina)
                    .map((pedido) => (
                      <tr key={pedido.id_historial}>
                        
                        <td>{pedido.nombre_receta}</td>
                        <td>{pedido.ingredientes}</td>
                        <td>{pedido.create_at}</td>
                        <td>{pedido.ready_at}</td>
                        {/*<td>{pedido.hielo}</td>*/}
                        <td>{pedido.hielo === 1 ? "Sí" : "No"}</td>
                        <td>{pedido.costoBebida}</td>
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
      
      <Col>
        <h5>Consumo de Bebidas</h5>
        <ApexCharts options={bebidasChartSettings} series={[{ data: bebidasSeries }]} type="bar" height={300} />
      </Col>
      <Col>
        <h5>Uso de Ingredientes</h5>
        <ApexCharts options={ingredientesChartSettings} series={ingredientesSeries} type="pie" height={300} />
      </Col>
      
      {/* Gráfico de bebidas por día */}
      <div style={{ marginTop:'20px', marginBottom: "20px" }}>
        <h4>Registro de Bebidas Totales por Día</h4>
        <BebidasPorDiaChart pedidosFiltrados={pedidosFiltrados} />
      </div>

      <div style={{ marginTop:'50px', display:'flex', width:'100%', height:'50px', justifyContent:'center'}}>
        {/*
        <button className={s.nBotonRecetas} onClick={eliminarPedido}>
          <p>Eliminar Toda la Tabla de Pedidos</p>
        </button>
        */}
        <button className={s.nBotonRecetas} onClick={handleShowConfirmModal}>
          <p>Eliminar Toda la Tabla de Pedidos</p>
        </button>
      </div>

      {/* Modal de confirmación para eliminar receta */}
      <Modal 
        isOpen={showConfirmModal} 
        toggle={handleCloseConfirmModal}
        onClick={(e) => {
          // Detecta si el clic fue fuera del modal
          if (e.target.classList.contains("modal")) {
            handleCloseConfirmModal();  // Cierra el modal si se hace clic fuera de él
          }
        }} 
        style={{
          overlay: { backgroundColor: 'rgba(255, 139, 5, 0.7)' },
          content: { maxWidth: '500px', maxHeight:'320px', margin: 'auto', padding: '20px', borderRadius: '10px' }
        }}
        
      >
        <ModalBody>
        <div className="d-flex flex-column justify-content-center">
          <h3 className="d-flex  justify-content-center align-content-center">
            Confirmar eliminación
          </h3>
          <p className="d-flex  justify-content-center mt-3">
            ¿Estás seguro de que deseas eliminar toda la Tabla?
          </p>
          <div className='d-flex  justify-content-center mt-4' >

            <Button className={s.nBotonRecetas} onClick={handleConfirmDelete}>Borrar Tabla</Button>
            
            <Button 
              color="secondary" 
              onClick={handleCloseConfirmModal}
              className={`${s.nBotonRecetas} ml-2`}
            >
              Cancelar
            </Button>
          </div>
        </div>
        </ModalBody>
      </Modal>
      
    </div>
  );
};

export default Tables;
