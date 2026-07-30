export enum ClothingCategory {
  TOPS = 'tops',
  BOTTOMS = 'bottoms',
  DRESSES = 'dresses',
  OUTERWEAR = 'outerwear',
  SHOES = 'shoes',
  ACCESSORIES = 'accessories',
}

export interface User {
  id: number;
  email: string;
  created_at: string;
}

export interface ClothingItem {
  id: number;
  user_id: number;
  name: string;
  category: ClothingCategory;
  image_filename: string | null;
  created_at: string;
  updated_at: string;
}

export interface ClothingItemCreate {
  name: string;
  category: ClothingCategory;
}

export interface ClothingItemUpdate {
  name?: string;
  category?: ClothingCategory;
  image_filename?: string;
}

export interface AuthState {
  isAuthenticated: boolean;
  user: User | null;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}
