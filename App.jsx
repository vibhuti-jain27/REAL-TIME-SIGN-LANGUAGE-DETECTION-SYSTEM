import React from 'react';
import '../../static/css/App.css';
import HeroSection from './HeroSection';
// import UploadPage from './components/uploadPage'; 
// import Results from './components/results';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  // let session_id;
  // let password;
  // let target;
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HeroSection />} />
        {/* <Route path="/upload" element={<UploadPage />} />
        <Route path="/results" element={<Results session_id={session_id} password={password} target={target}/>} /> */}
      </Routes>
    </Router>
  );
}

export default App;
