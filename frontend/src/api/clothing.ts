import type { ClothingItem, ClothingItemCreate, ClothingItemUpdate } from '../types';

export async function fetchClothing(): Promise<ClothingItem[]> {
  throw new Error('not implemented');
}

export async function createClothing(_data: ClothingItemCreate): Promise<ClothingItem> {
  throw new Error('not implemented');
}

export async function updateClothing(_id: number, _data: ClothingItemUpdate): Promise<ClothingItem> {
  throw new Error('not implemented');
}

export async function deleteClothing(_id: number): Promise<void> {
  throw new Error('not implemented');
}
