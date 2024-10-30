import React, { useState, useEffect } from 'react';
import { Button, FormGroup, Label, Input } from 'reactstrap';
import Select from 'react-select'; // Select con buscador integrado
import s from "../ingredientes/Ingredientes.module.scss";
// Notificaciones
import { toast } from "react-toastify";
import Notification from "../../components/Notification/Notification.js";


const NuevaReceta = ({ onClose, setRecetas, recetas, receta, modoEditar, ingredientes }) => {

  //Config de Notificaciones
  const options = {
    autoClose: 3000,
    closeButton: false,
    hideProgressBar: true,
    position: toast.POSITION.TOP_CENTER,
  };

  const [createRecStatus, setCreateRecStatus] = useState({});
  const [modifyRecStatus, setModifyRecStatus] = useState({});
  const ingredientesPorDefecto = ingredientes.length > 0 ? ingredientes : [
    { nombre: 'Ron', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Vodka', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Tequila', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Whiskey', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Triple Sec', tipo: 'Alcohol', costo: '1.23', cantidad: '750' }
  ];
  const [idReceta, setIdReceta] = useState(receta ? receta.id_receta : '');
  const [nombreReceta, setNombreReceta] = useState(receta ? receta.nombre : '');
  const [ingredientesSeleccionados, setIngredientesSeleccionados] = useState(
    receta ? receta.ingredientes.map(ing => ({ label: ing.nombre, value: ing })) : []
  );

  const opcionesIngredientes = [
    { label: "Vacío", value: null },
    ...ingredientesPorDefecto.map(ing => ({ label: ing.nombre, value: ing }))
  ];

  const manejarCambioIngrediente = (index, ingrediente) => {
    const nuevosIngredientes = [...ingredientesSeleccionados];
    nuevosIngredientes[index] = ingrediente;
    setIngredientesSeleccionados(nuevosIngredientes);
  };

  const guardarReceta = () => {
    const nuevaReceta = {
      id_receta: idReceta,
      nombre: nombreReceta,
      ingredientes: ingredientesSeleccionados.filter(ing => ing.value !== null).map(ing => ing.value)
    };

    if (modoEditar) {
      fetch('/receta/modificar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(nuevaReceta)
      })
      .then(response => {
          console.log('Respuesta del servidor:', response); // Log de la respuesta
          return response.json();
      })
      .then(data => {
          console.log('Datos recibidos:', data); // Log de los datos recibidos
          setModifyRecStatus(data); // Guarda la respuesta en createIngStatus
          onClose(); // Llamar a onClose() solo después de recibir la respuesta del servidor
      })
      .catch(error => console.error('Error:', error));
    } else {
      fetch('/receta/nuevo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(nuevaReceta)
      })
      .then(response => {
          console.log('Respuesta del servidor:', response); // Log de la respuesta
          return response.json();
      })
      .then(data => {
          console.log('Datos recibidos:', data); // Log de los datos recibidos
          setCreateRecStatus(data); // Guarda la respuesta en createIngStatus
          onClose(); // Llamar a onClose() solo después de recibir la respuesta del servidor
      })
      .catch(error => console.error('Error:', error));
    }
    
    
  };

  useEffect(() => {
    console.log('Estado de modifyRecStatus:', modifyRecStatus);
    
    if (modifyRecStatus.code > 0){
      
      toast(
        
        <Notification 
            type={modifyRecStatus.status} 
            errorMessage={modifyRecStatus.message} 
            withIcon 
        />, 
        options
      );
      
    } 
  }, [modifyRecStatus]);
  useEffect(() => {
    console.log('Estado de createRecStatus:', createRecStatus);
    
    if (createRecStatus.code > 0){
      
      toast(
        
        <Notification 
            type={createRecStatus.status} 
            errorMessage={createRecStatus.message} 
            withIcon 
        />, 
        options
      );
      
    }
  }, [createRecStatus]);

  return (
    <div className={s.total}>
      <div className={s.cuadroGeneral}>
        <h2>{modoEditar ? 'Editar Receta' : 'Crear Nueva Receta'}</h2>
        
        <FormGroup>
          {modoEditar && (
            <>
              <Label for="id_receta">ID de la Receta</Label>
              <Input
                type="text"
                id="id_receta"
                value={idReceta}
                disabled={modoEditar}
              />
            </>
          )}
          <Label for="nombreReceta">Nombre de la Receta</Label>
          <Input
            type="text"
            id="nombreReceta"
            value={nombreReceta}
            onChange={(e) => setNombreReceta(e.target.value)}
            placeholder="Introduce el nombre de la receta"
          />

        </FormGroup>

        {/* Contenedor en una sola columna */}
        <div className={s.recetaContainer}>
          {[...Array(10)].map((_, index) => (
            <div key={index} className={s.recetaFila}>
              <Label className={s.nlabel}>Ingrediente {index + 1}</Label>
              <Select
                className={s.ingredienteRecetaSelector}
                value={ingredientesSeleccionados[index] || { nlabel: "Vacío", value: null }}
                onChange={(ingrediente) => manejarCambioIngrediente(index, ingrediente)}
                options={opcionesIngredientes}
                isSearchable={true}
                placeholder={`Selecciona ingrediente ${index + 1}`}
              />
            </div>
          ))}
        </div>

        <div className="d-flex justify-content-center mt-4">
          <Button className={`${s.nBotonRecetas} mr-3`} onClick={guardarReceta}>Guardar Receta</Button>
          <Button className={s.nBotonRecetas} onClick={onClose}>Cancelar</Button>
        </div>
        <div className='mb-5'></div>
        <hr></hr>
        <div className='mb-4'></div>
      </div>
    </div>
  );
};

export default NuevaReceta;
