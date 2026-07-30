import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import WardrobePage from './pages/WardrobePage';

function LandingPage() {
  return <h1>Willkommen</h1>;
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/wardrobe" element={<WardrobePage />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
