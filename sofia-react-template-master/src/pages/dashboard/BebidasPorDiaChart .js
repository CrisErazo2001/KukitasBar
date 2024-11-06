import React from "react";
import ApexCharts from "react-apexcharts";
import dayjs from "dayjs"; // Usamos dayjs para manejar fechas

export default function BebidasPorDiaChart({ pedidosFiltrados }) {
  // Paso 1: Procesar pedidos para obtener el total de bebidas por día
  const bebidasPorDia = pedidosFiltrados.reduce((acc, pedido) => {
    const fecha = dayjs(pedido.create_at).format("YYYY-MM-DD"); // Obtener solo la fecha
    acc[fecha] = (acc[fecha] || 0) + 1; // Contar cada pedido en la fecha correspondiente
    return acc;
  }, {});

  // Datos para las series (total de bebidas por día)
  const series = [
    {
      name: "Total de Bebidas",
      type: "column", // Tipo de gráfico columna
      data: Object.values(bebidasPorDia), // Contador de pedidos por fecha
    },
  ];

  const chartSettings = {
    colors: ["#FF5668"], // Color de la barra
    chart: {
      height: "100%", // Responsivo
      type: "line", // Tipo de gráfico: línea
      toolbar: {
        show: false, // Sin barra de herramientas
      },
    },
    stroke: {
      curve: "smooth", // Curvatura suave en la línea
      width: [0, 1], // Ancho de la línea
    },
    dataLabels: {
      enabled: true, // Mostrar etiquetas de datos en el gráfico
      style: {
        fontSize: "12px",
        fontWeight: 500,
      },
      background: {
        borderWidth: 0, // Sin borde en el fondo de los datos
      },
    },
    labels: Object.keys(bebidasPorDia), // Fechas como etiquetas en el eje X
    xaxis: {
      type: "category",
      labels: {
        style: {
          colors: "#6B859E", // Color de las etiquetas en el eje X
        },
      },
    },
    yaxis: [
      {
        title: {
          text: "Total de Bebidas", // Título del eje Y
          style: {
            fontSize: "12px",
            fontWeight: 400,
            color: "#6B859E",
          },
        },
        labels: {
          style: {
            colors: ["#6B859E"], // Color de las etiquetas en el eje Y
          },
        },
      },
    ],
    fill: {
      type: "solid", // Llenado sólido para las columnas
      opacity: 1,
    },
    responsive: [
      {
        breakpoint: 600, // En pantallas menores de 600px (celulares)
        options: {
          chart: {
            height: 300, // Ajustar altura para pantallas pequeñas
          },
          xaxis: {
            labels: {
              rotate: -45, // Rotar etiquetas en pantallas pequeñas
            },
          },
        },
      },
    ],
  };

  return (
    <ApexCharts
      options={chartSettings}
      series={series}
      type="line"
      height="100%" // Ajuste para el contenedor responsivo
    />
  );
}
