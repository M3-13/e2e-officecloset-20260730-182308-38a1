import { createContext, useContext, useMemo, type ReactNode } from 'react';
import type { AuthState } from '../types';

interface AuthContextValue extends AuthState {
  login: (_email: string, _password: string) => Promise<void>;
  register: (_email: string, _password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const value = useMemo<AuthContextValue>(() => ({
    isAuthenticated: false,
    user: null,
    login: async () => { throw new Error('not implemented'); },
    register: async () => { throw new Error('not implemented'); },
    logout: () => { throw new Error('not implemented'); },
  }), []);

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return ctx;
}
