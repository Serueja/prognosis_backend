import React from 'react';
import './App.css';
import Header from './components/Header/Header';
import Navbar from './components/Navbar/Navbar';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import Month_first from './components/Month/Month_first';



const HomePage = (props) => {
    return (
     <div className='app-wrapper' >
        <Header />
        <Navbar />
    </div>
    )
} 
const App = (props) => {

    return <BrowserRouter>
                <Routes>
                <Route exact path="/"
                        element={<HomePage />} />

                    <Route  path="/:id"
                        element={<Month_first />} />      
                </Routes>
    </BrowserRouter>

   
}

export default App;