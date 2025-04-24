import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import LoginForm from './components/Login';
import Footer from './components/footer';
import Cart from './components/Cart';
import HomePage from './components/Home';
import ProductCard from './components/product';

function App() {
  const [cart, setCart] = useState([]);
  const [badgeCount, setBadgeCount] = useState(0);

  const updateBadgeCount = (count) => {
    setBadgeCount(count);
  };

  const addToCart = (product) => {
    setCart([...cart, product]);
    updateBadgeCount(cart.length + 1);
  };
  const removeFromCartFunction = (product) => {
    // Implement the logic to remove the product from the cart
    const updatedCart = cart.filter((item) => item.id !== product.id);
    setCart(updatedCart);
    updateBadgeCount(updatedCart.length);
  };

  const updateQuantityFunction = (product, newQuantity) => {
    // Implement the logic to update the quantity of the product in the cart
    const updatedCart = cart.map((item) => {
      if (item.id === product.id) {
        return { ...item, quantity: newQuantity };
      }
      return item;
    });
    setCart(updatedCart);
  };

  return (
    <Router>
      <Navbar totalItemsInCart={badgeCount} />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginForm />} />
        <Route
          path="/cart"
          element={
            <Cart
              cart={cart}
              removeFromCart={removeFromCartFunction}
              updateQuantity={updateQuantityFunction}
            />
          }
        />
        <Route
          path="/products"
          element={<ProductCard addToCart={addToCart} />}
        />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;