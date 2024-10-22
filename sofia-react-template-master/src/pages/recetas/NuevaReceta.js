import React, { useState } from 'react';
import { Button, Col, Row, FormGroup, Label, Input } from 'reactstrap';
import Select from 'react-select'; // Select con buscador integrado
import s from "../ingredientes/Ingredientes.module.scss";

const NuevaReceta = ({ onClose, setRecetas, recetas, receta, modoEditar, ingredientes }) => {
  // Ingredientes quemados para evitar errores si no se pasan dinámicamente
  const ingredientesPorDefecto = ingredientes.length > 0 ? ingredientes : [
    { nombre: 'Ron', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Vodka', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Tequila', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Whiskey', tipo: 'Alcohol', costo: '1.23', cantidad: '750' },
    { nombre: 'Triple Sec', tipo: 'Alcohol', costo: '1.23', cantidad: '750' }
  ];

  // Valores quemados por defecto si no hay receta seleccionada
  const [nombreReceta, setNombreReceta] = useState(receta ? receta.nombre : '');
  const [ingredientesSeleccionados, setIngredientesSeleccionados] = useState(
    receta ? receta.ingredientes.map(ing => ({ label: ing.nombre, value: ing })) : []
  );

  // Opciones del selector (con la opción "vacío" añadida)
  const opcionesIngredientes = [
    { label: "Vacío", value: null },
    ...ingredientesPorDefecto.map(ing => ({ label: ing.nombre, value: ing }))
  ];

  // Manejar cambios en los selectores
  const manejarCambioIngrediente = (index, ingrediente) => {
    const nuevosIngredientes = [...ingredientesSeleccionados];
    nuevosIngredientes[index] = ingrediente;
    setIngredientesSeleccionados(nuevosIngredientes);
  };

  // Manejar la creación/edición de la receta
  const guardarReceta = () => {
    const nuevaReceta = {
      nombre: nombreReceta,
      ingredientes: ingredientesSeleccionados.filter(ing => ing.value !== null).map(ing => ing.value)
    };

    if (modoEditar) {
      // Si estamos editando, reemplazamos la receta existente
      const recetasActualizadas = recetas.map(rec =>
        rec.nombre === receta.nombre ? nuevaReceta : rec
      );
      setRecetas(recetasActualizadas);
    } else {
      // Si estamos creando, añadimos la nueva receta
      setRecetas([...recetas, nuevaReceta]);
    }

    onClose(); // Cerrar el formulario
  };

  return (
    <div className={s.total}>
      <div className={s.cuadroGeneral}>
        <h2>{modoEditar ? 'Editar Receta' : 'Crear Nueva Receta'}</h2>
        
        <FormGroup>
          <Label for="nombreReceta">Nombre de la Receta</Label>
          <Input
            type="text"
            id="nombreReceta"
            value={nombreReceta}
            onChange={(e) => setNombreReceta(e.target.value)}
            placeholder="Introduce el nombre de la receta"
          />
        </FormGroup>

        <Row>
          {[...Array(10)].map((_, index) => (
            <Col xs={12} key={index} className="mb-3">
              <Label>Ingrediente {index + 1}</Label>
              <Select
                value={ingredientesSeleccionados[index] || { label: "Vacío", value: null }}
                onChange={(ingrediente) => manejarCambioIngrediente(index, ingrediente)}
                options={opcionesIngredientes}
                isSearchable={true}
                placeholder={`Selecciona ingrediente ${index + 1}`}
              />
            </Col>
          ))}
        </Row>
        <div className='mb-5'></div>
        <div className="d-flex justify-content-center">
          <Button className={`${s.nBotonRecetas} mr-3`} onClick={guardarReceta}>Guardar Receta</Button>
          <Button className={s.nBotonRecetas} onClick={onClose}>Cancelar</Button>
        </div>
        <div className='mb-5'></div>
      
      </div>
      <hr />
      <div className='mb-5'></div>
    </div>
  );
};

export default NuevaReceta;
