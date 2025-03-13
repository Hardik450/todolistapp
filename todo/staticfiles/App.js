import React from 'react';
import ReactDOM from 'react-dom/client';
import { Link } from 'react-router-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path='about' element={<About />} />
          <Route path='contact' element={<Contact />} />
          <Route path='workspace' element={<Workspace />} />
          <Route path='*' element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}
function Layout() {
  return (
    <div className='nav'>
      <ul>
        <li><Link to='/'>Home</Link></li>
        <li><Link to='/about'>About</Link></li>
        <li><Link to='/contact'>Contact</Link></li>
        <li><Link to='/workspace'>Workspace</Link></li>
      </ul>
    </div>
  )
}
function Home() {
  return (
    <>
      <Layout />
      <h1> Hello, World!</h1>
    </>
  )
}
function Workspace() {
  return (
    <>
      <Layout />
      <h1> Hello, World!<br /> This is Workspace.</h1>
    </>
  )
}
function About() {
  return (
    <>
      <Layout />
      <h1> Hello, World!<br /> This is about page.</h1>
    </>
  )
}
function Contact() {
  return (
    <>
      <Layout />
      <h1> Hello, World!.<br />This is contact page.</h1>
    </>
  )
}
function NotFound() {
  return (
    <>
      <Layout />
      <h1>404</h1>
    </>
  )
}

ReactDOM.createRoot(document.querySelector('#root')).render(<App />)

export default App;
