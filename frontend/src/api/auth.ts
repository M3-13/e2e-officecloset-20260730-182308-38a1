import type { TokenResponse } from '../types';

export async function login(email: string, _password: string): Promise<TokenResponse> {
  void email;
  throw new Error('not implemented');
}

export async function register(email: string, _password: string): Promise<void> {
  void email;
  throw new Error('not implemented');
}

export function logout(): void {
  throw new Error('not implemented');
}
