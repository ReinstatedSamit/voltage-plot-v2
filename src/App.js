import React from "react";
import "./App.scss";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle";

import Header from "./components/Header";
import PlotComponent from "./components/PlotComponent";

function App() {
  return (
    <div className='App'>
      <Header />
      <PlotComponent />
    </div>
  );
}

export default App;
